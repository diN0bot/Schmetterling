from django.db import models
from django.contrib import admin
from django.conf import settings

from lib import choice_field_utils
from lib import enumerator


class Box(models.Model):
    identifier = models.SlugField()
    name = models.CharField(max_length=100)

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


def _leaf_choicifier(key):
    return key[:2] + key[3]

class Leaf(models.Model):
    identifier = models.SlugField()
    name = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True)

    TYPES_CHOICES = choice_field_utils.create_type_choices(settings.LEAF_TYPES,
                                                           func=_leaf_choicifier)
    TYPES = enumerator.enum_from_choices(TYPES_CHOICES)

    type = models.CharField(max_length=choice_field_utils.max_length_item(TYPES.ALL_ENUMS),
                            choices=TYPES_CHOICES)
