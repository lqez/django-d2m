version_info = (0, 1, 4)

__version__ = VERSION = '.'.join(map(str, version_info))

from .d2m import queryset_to_model, list_to_model, dict_to_model

__all__ = ['queryset_to_model', 'list_to_model', 'dict_to_model']
