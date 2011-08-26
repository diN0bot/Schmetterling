from django.db import models
from django.contrib import admin
from django.conf import settings

from lib import choice_field_utils
from lib import enumerator
from lib import jsonfield

import unique_slugify

import pygithub
import pyvo

import copy
import config

github = pygithub.Github(config.gh_user, config.gh_pass)
vo = pyvo.VersionOne(config.vo_user, config.vo_pass)

def _leaf_choicifier(key):
    return key[:2] + key[3]

class Leaf(models.Model):
    """
    A thing that lives in boxes
    """
    TYPES_CHOICES = choice_field_utils.create_type_choices(settings.LEAF_TYPES,
                                                           func=_leaf_choicifier)
    TYPES = enumerator.enum_from_choices(TYPES_CHOICES)

    # everything worth anything has a unique URL
    url = models.URLField(unique=True)
    # a slug type unique thing
    identifier = models.SlugField()
    # something human readable
    name = models.CharField(max_length=100)
    # the thing's data
    data = jsonfield.JSONField()
    # the kind of thing
    type = models.CharField(max_length=choice_field_utils.max_length_item(TYPES.ALL_ENUMS),
                            choices=TYPES_CHOICES)

    def __init__(self, *args, **kw):
        super(Leaf, self).__init__(*args, **kw)
        self._old_data = self.data

    def save(self, **kwargs):
        unique_slugify.unique_slugify(self, self.name, slug_field_name='identifier')
        if self.pk and self.data != self._old_data:
            self.update_attributes()
            super(Leaf, self).save()
        super(Leaf, self).save()

    def update_attributes(self):
        changed_dict = self.dictdiff(self._old_data, self.data)
        if self.type == 'VO_ISSUE':
            task = pyvo.task.task(pyvo.core.url_open(self.uri))
            for key, item in changed_dict.items():
                task.__setattr__(key, item)
        if self.type == 'GH_ISSUE':
            issue = github.get_issue(self.data['url'][22:])
            for key, item in changed_dict.items():
                issue.__setattr__(key, item)

    def dictdiff(self, d1, d2):
        diff= (set(self.comdict(d2))-set(self.comdict(d1)))
        diff = dict(diff)
        return diff

    def comdict(self, d):
        print d
        if isinstance(d, dict):
            for item in d.items():
                    if isinstance(item[1], dict):
                        d[item[0]] = self.comdict(item[1])
                    if isinstance(item[1], list):
                        d[item[0]] = self.comdict(item[1])
            print d.items()
            return tuple(d.items())
        else:
            for index, item in enumerate(d):
                    if isinstance(item, dict):
                        d[index] = self.comdict(item)
                    if isinstance(item, list):
                        d[index] = self.comdict(item)
            return tuple(d)

class Person(models.Model):
    """
    An entity assigned to boxes
    """
    name = models.CharField(max_length=100)
    # things that represent this person, eg user pages and usernames in project apps
    leaves = models.ManyToManyField('Leaf', null=True, blank=True)

class Box(models.Model):
    """
    A simple multi-hierarchical container.
    Multi in the sense that a Box may be contained in multiple Boxes!
    """
    STATES_CHOICES = choice_field_utils.create_type_choices(settings.BOX_STATES,
                                                            func=_leaf_choicifier)
    STATES = enumerator.enum_from_choices(STATES_CHOICES)

    identifier = models.SlugField()
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=choice_field_utils.max_length_item(STATES.ALL_ENUMS),
                             choices=STATES_CHOICES)
    user = models.ForeignKey(Person)

    boxes = models.ManyToManyField('self', null=True, blank=True)
    leaves = models.ManyToManyField('Leaf', null=True, blank=True)

    admin_options = {'prepopulated_fields': {"identifier": ("name",)} }

    def nest_in(self, box):
        box.boxes.add(self)

    def unnest_from(self, box):
        box.boxes.remove(self)

    def unnest(self):
        for box in Box.objects.filter(boxes=self):
            self.unnest_from(box)
