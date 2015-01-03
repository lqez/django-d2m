django-d2m
==========

.. image:: https://travis-ci.org/lqez/django-d2m.svg?branch=master
    :target: https://travis-ci.org/lqez/django-d2m
.. image:: https://img.shields.io/coveralls/lqez/django-d2m.svg
    :target: https://coveralls.io/r/lqez/django-d2m?branch=master

Mapping annotated dict list into Django models


Usage
-----

Wrap your django queryset or list with django-d2m functions

.. code:: python 

    from django_d2m import queryset_to_model

    queryset = CashUsageLog.objects.values('product__episode__comic').annotate(cash_used=Sum('cash'))
    i_want_real_objects = queryset_to_model(queryset)

    # You can convert just a dict
    from django_d2m import dict_to_model
    dict_to_model(some_dict_contains_only_id, MyModel)

    # Or, for list
    from django_d2m import list_to_model
    list_to_model(some_dict_list, YourModel)


Before
------

.. code:: text 

    {'product__episode__comic': 10L, 'cash_used': 3100}
    {'product__episode__comic': 7L, 'cash_used': 1100}
    {'product__episode__comic': 15L, 'cash_used': 800}

After
-----

.. code:: text 

    {'product__episode__comic': <Comic: 다즐짱>, 'cash_used': 3100}
    {'product__episode__comic': <Comic: 파이일기>, 'cash_used': 1100}
    {'product__episode__comic': <Comic: 스카리의 유희>, 'cash_used': 800}


Install
-------

.. code:: shell

    pip install django-d2m


License
-------

MIT


Author
------

@lqez
