
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book                       #book.models weil ja aus anderer app ko,,t das models

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = 'Django for Beginners',
            subtitle = 'subtitle',
            author = 'W. Vincent',
            isbn='1234567890'
        )

    def test_api_listview(self):
        response = self.client.get(reverse('booklist'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)   # man kann auch einfach 200 schreiben, das ist hier für readability
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(len(Book.objects.all()), 1)  # das gleiche wie zeile drüber nur mit len anstatt ćount
        self.assertContains(response, self.book)
