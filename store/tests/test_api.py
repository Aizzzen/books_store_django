from django.urls import reverse
from rest_framework.test import APITestCase

from store.models import Books
from store.serializers import BooksSerializer


class BooksAPITestCase(APITestCase):
    def test_get(self):
        book1 = Books.objects.create(name='Test Book-1', price=25)
        book2 = Books.objects.create(name='Test Book-2', price=50)
        url = reverse('books-list')
        response = self.client.get(url)
        serializer_data = BooksSerializer([book1, book2], many=True).data
        self.assertEqual(serializer_data, response.data)
        print(response.data)
