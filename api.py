from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
#from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from data_store.models import Box, Leaf, Person


class BoxResource(ModelResource):
    class Meta:
            queryset = Box.objects.all()
            #authorization = Authorization()
            # Add it here.
            authentication = BasicAuthentication()
            authorization = DjangoAuthorization()

class LeafResource(ModelResource):
    class Meta:
            queryset = Leaf.objects.all()
            limit = 100000
            default_format = 'application/json'
            #authorization = Authorization()
            # Add it here.
            authentication = BasicAuthentication()
            authorization = DjangoAuthorization()

class PersonResource(ModelResource):
    class Meta:
            queryset = Person.objects.all()
            #authorization = Authorization()
            # Add it here.
            authentication = BasicAuthentication()
            authorization = DjangoAuthorization()

