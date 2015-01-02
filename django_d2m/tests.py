from django_d2m.testapp.models import Author, Tag, Article
from django_d2m import dict_to_model
from django.test import TestCase


class D2MTestCase(TestCase):
    def setUp(self):
        author_lqez = Author.objects.create(name='lqez')
        tag_diary = Tag.objects.create(name='diary')
        tag_blah = Tag.objects.create(name='blah')

        article = Article.objects.create(
            subject='foobar',
            body='ohmygod',
            read=150,
            author=author_lqez
        )
        article.tags.add(tag_diary)
        article.tags.add(tag_blah)

    def test_base(self):
        self.assertTrue(True)

    def test_basic(self):
        from django.db.models import Sum

        read_counts = Article.objects.values('author').annotate(total_read=Sum('read'))
        dict_to_model(read_counts)
