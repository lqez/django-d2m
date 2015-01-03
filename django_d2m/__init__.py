version_info = (0, 1, 0)

__version__ = VERSION = '.'.join(map(str, version_info))
__project__ = PROJECT = 'django-d2m'

from django.db.models import ForeignKey
from django.db.models.fields import FieldDoesNotExist
from collections import defaultdict

__all__ = ['dictlist_to_model', ]


def _get_field_class_matching(base_model, d):
    class NotForeignKey(Exception):
        pass

    result = {}

    for k in d.keys():
        model = base_model

        try:
            for field in k.split('__'):
                field_object, _, direct, m2m = \
                    model._meta.get_field_by_name(field)
                if not m2m and direct and isinstance(field_object, ForeignKey):
                    model = field_object.rel.to
                else:
                    raise NotForeignKey

            result[k] = model
        except FieldDoesNotExist, NotForeignKey:
            continue

    return result


def queryset_to_model(qs, basemodel=None):
    # Convert queryset to list
    if isinstance(qs, list):
        qs = list(qs)

    # Raise when None
    if len(qs) == 0:
        raise ValueError

    # Get field matching table with first one
    matches = _get_field_class_matching(basemodel if basemodel else qs.model,
                                        qs[0])

    # Pull out candidates from ids
    candidates = defaultdict(dict)
    for k, model in matches.iteritems():
        for obj in model.objects.filter(id__in=set([_[k] for _ in qs])):
            candidates[k][obj.id] = obj

    # Convert result with candidates
    result = []
    for item in qs:
        for k, v in candidates.iteritems():
            item[k] = v[item[k]]
        result.append(item)

    return result


def list_to_model(l, basemodel):
    return queryset_to_model(l, basemodel)


def dict_to_model(d, basemodel):
    # Get field matching table with first one
    matches = _get_field_class_matching(basemodel, d)

    # Convert
    for k, model in matches.iteritems():
        d[k] = model.objects.get(id=d[k])

    return d
