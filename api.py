from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from data_store.models import Box, Leaf, Person


class BoxResource(ModelResource):
    class Meta:
            queryset = Box.objects.all()

class LeafResource(ModelResource):
    class Meta:
            queryset = Leaf.objects.all()
            authorization= Authorization()

class PersonResource(ModelResource):
    class Meta:
            queryset = Person.objects.all()
