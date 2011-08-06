
def _default_choicifier_func(key):
    return key[:2]

def create_type_choices(alist, func=_default_choicifier_func):
    # contains abbreviated choices
    abrvs = {}
    tuples = []
    for key in alist:
        abrv = func(key)
        if abrv in abrvs:
            abrvs[abrv] += 1
            abrv += str(abrvs[abrv] - 1)
        abrvs[abrv] = 0
        tuples.append((abrv, key))

    return tuple(tuples)

def max_length_item(alist):
    return reduce(lambda x, y: max(len(str(x)), len(str(y))), alist)
