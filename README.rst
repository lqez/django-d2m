django-d2m
==========

Mapping annotated dict list into Django models


Usage
-----

Wrap your django queryset or list with django-d2m functions

.. code:: python 

    from django_d2m import queryset_to_model

    queryset = CashUsageLog.objects.values('product__episode__comic').annotate(cash_used=Sum('cash'))
    i_want_this = queryset_to_model(queryset)


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


License
-------

MIT


Author
------

@lqez
