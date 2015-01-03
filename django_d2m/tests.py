from django_d2m.testapp.models import Author, Tag, Article, Country
from django_d2m import dict_to_model, list_to_model, queryset_to_model
from django.db.models import Sum, Count
from django.test import TestCase


class D2MTestCase(TestCase):
    def assertDictList(self, l1, l2, order_by=None):
        if order_by:
            from operator import itemgetter
            l1, l2 = [sorted(_, key=itemgetter(order_by))
                      for _ in (l1, l2)]

        pairs = zip(l1, l2)
        self.assertFalse(any(x != y for x, y in pairs))

    def test_base(self):
        self.assertTrue(True)

    def test_dict_to_model(self):
        author_lqez = Author.objects.get(name='lqez')

        result = dict_to_model(
            Article.objects.filter(author=author_lqez)
            .values('author').annotate(total_read=Sum('read'))[0],
            Article
        )

        self.assertEqual(result['total_read'], 200)

    def test_list_to_model(self):
        result = list_to_model(
            list(Article.objects.values('author')
                 .annotate(total_read=Sum('read'))),
            Article
        )

        expected = [
            {'total_read': 200,
             'author': Author.objects.get(name='lqez')},
            {'total_read': 1000,
             'author': Author.objects.get(name='Prodo')},
            {'total_read': 30000,
             'author': Author.objects.get(name='Tolkien')},
        ]

        self.assertDictList(result, expected, 'total_read')

    def test_queryset_to_model(self):
        result = queryset_to_model(
            Article.objects.values('tags')
            .annotate(count=Count('tags'))
        )

        expected = [
            {'count': 3,
             'tags': Tag.objects.get(name='Diary')},
            {'count': 5,
             'tags': Tag.objects.get(name='Fiction')},
            {'count': 1,
             'tags': Tag.objects.get(name='IT')},
        ]

        self.assertDictList(result, expected, 'count')

    def test_double(self):
        result = queryset_to_model(
            Article.objects.values('author__country')
            .annotate(total_read=Sum('read'))
        )

        expected = [
            {'total_read': 200,
             'author__country': Country.objects.get(name='Korea')},
            {'total_read': 31000,
             'author__country': Country.objects.get(name='Endor')},
        ]

        self.assertDictList(result, expected, 'total_read')
