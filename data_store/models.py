from django.db import models
from django.contrib import admin
from django.conf import settings

from lib import choice_field_utils
from lib import enumerator
from lib import jsonfield

import unique_slugify

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

    def save(self, **kwargs):
        unique_slugify.unique_slugify(self, self.name, slug_field_name='identifier')
        super(Leaf, self).save()

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
