
# copied from http://djangosnippets.org/snippets/377/
# some edits made

from django.db import models
from django.utils import simplejson as json

from django.core.serializers.json import DjangoJSONEncoder

class JSONField(models.TextField):

    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        """
        @param value: JSON string or Python object
        @return: Python object
        """
        if isinstance(value, basestring):
            # when setting model fields, this will be called
            # with the python object.
            if value:
                return json.loads(value)
            else:
                return '{}'
        else:
            return value

    def get_prep_value(self, value):
        """
        @param value: Python object
        @return: JSON string
        """
        return json.dumps(value, cls=DjangoJSONEncoder)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
