from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Books
from store.serializers import BooksSerializer


class BooksAPITestCase(APITestCase):
    def setUp(self):
        self.book1 = Books.objects.create(name='Test Book-1', price=25, author='Author-1')
        self.book2 = Books.objects.create(name='Test Book-2', price=50, author='Author-1')
        self.book3 = Books.objects.create(name='Test Book Author-1', price=50, author='Author-2')

    def test_get(self):
        url = reverse('books-list')
        response = self.client.get(url)
        serializer_data = BooksSerializer([self.book1, self.book2, self.book3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('books-list')
        response = self.client.get(url, data={'price': 50})
        serializer_data = BooksSerializer([self.book2, self.book3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('books-list')
        response = self.client.get(url, data={'search': 'Author-1'})
        serializer_data = BooksSerializer([self.book1, self.book3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
