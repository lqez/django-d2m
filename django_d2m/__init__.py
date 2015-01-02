version_info = (0, 1, 0)

__version__ = VERSION = '.'.join(map(str, version_info))
__project__ = PROJECT = 'django-d2m'

from django.db.models import ForeignKey
from django.db.models.fields import FieldDoesNotExist
from collections import defaultdict

__all__ = ['dictlist_to_model', ]


def _get_conversion_table(base_model, d):
    class NotForeignKey(Exception):
        pass

    conversion_table = {}

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

            conversion_table[k] = model
        except FieldDoesNotExist, NotForeignKey:
            continue

    return conversion_table


def dict_to_model(dictlist):
    conversion_table = _get_conversion_table(dictlist.model, dictlist[0])
    candidates = defaultdict(dict)

    for k, model in conversion_table.iteritems():
        for obj in model.objects.filter(
            id__in=set([_[k] for _ in dictlist])
        ):
            candidates[k][obj.id] = obj

    result = []
    for item in dictlist:
        for k, v in candidates.iteritems():
            item[k] = v[item[k]]
        result.append(item)

    return result
