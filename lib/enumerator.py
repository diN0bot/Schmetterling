def _add_to_klass(attribute_map):
    """
    Returns type with instance fields based on attribute_map
    @param attribute_map: string, value map
    @return: type
    """
    def extra_attr_type(name, bases, dict_):
        dict_.update(attribute_map)
        return type(name, bases, dict_)
    return extra_attr_type

def _create_attribute_map(*args, **kwargs):
    """
    helper to create enum.Enumerator metaclass

    @param args: list of strings; become instance field names mapped to ints
    @param kwargs: dict of strings mapped to anything; keys become instance
      field names mapped to associated values
    @return: type with instance fields based on args and kwargs
      also inserts ALL_ENUMS and ALL_ENUM_VALUES
    """
    amap = kwargs.copy()
    amap.update([(v, k) for k, v in enumerate(args)])
    amap['ALL_ENUMS'] = set(kwargs.keys() + list(args))
    amap['ALL_ENUM_VALUES'] = set(kwargs.values() + [v[0] for v in enumerate(args)])
    return _add_to_klass(amap)

def enum(*args, **kwargs):
    """
    Creates immutable enumerator from args and kwargs.
    @param args: list of strings; will become instance fields mapped to ints
    @param kwargs: dictionary of strings mapped to values; will become
      instance fields mapped to associated values

    @return: Enumerator instance with fields based on args and kwargs

    Usage:
      Vowels = enum('a','e','i','o','u')
      Vowels.a # equals 0
      Vowels.e # equals 1
      Vowels.u = 22 # raises NotImplementedError

      VowelSounds = enum({'a': 'aaah', 'e': 'eeee'})
      VowelSounds.a # equals 'aaah'

      VowelSounds.ALL_ENUMS = ['a', 'e']
      VowelSounds.ALL_ENUM_VALUES = ['aaah', 'eeee']
    """

    class Enumerator(object):
        """
        Has immutable enumerator class attributes.
        """
        __metaclass__ = _create_attribute_map(*args, **kwargs)
        def __setattr__(self, name, value):
            """ enumerated fields are read-only """
            raise NotImplementedError
    return Enumerator()


def enum_from_choices(tuples):
    return enum(**dict([(y, x) for x, y in tuples]))
