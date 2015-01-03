from django_d2m.testapp.models import Author, Tag, Article
from django_d2m import dict_to_model, list_to_model, queryset_to_model
from django.db.models import Sum
from django.test import TestCase


class D2MTestCase(TestCase):
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

        from operator import itemgetter
        l1, l2 = [sorted(_, key=itemgetter('total_read'))
                  for _ in (result, expected)]

        pairs = zip(l1, l2)
        self.assertFalse(any(x != y for x, y in pairs))
