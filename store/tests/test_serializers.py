from unittest import TestCase

from store.models import Books
from store.serializers import BooksSerializer


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        book1 = Books.objects.create(name='Test Book-1', price=25)
        book2 = Books.objects.create(name='Test Book-2', price=50)
        data = BooksSerializer([book1, book2], many=True).data
        expected_data = [
            {
                'id': book1.id,
                'name': 'Test Book-1',
                'price': '25.00'
            },
            {
                'id': book2.id,
                'name': 'Test Book-2',
                'price': '50.00'
            },
        ]
        self.assertEqual(expected_data, data)
