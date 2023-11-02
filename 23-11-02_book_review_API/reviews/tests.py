from django.test import TestCase
from .models import Book, Review

class BookReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = 'Ein Titel',
            author = 'Mr X'
            )
        cls.review = Review.objects.create(
            book=cls.book, 
            review_text="Test Review", 
            rating=5)
    
    def test_book_content(self):
        self.assertEqual(self.book.title, 'Ein Titel')
        self.assertEqual(self.book.author, 'Mr X')
        self.assertEqual(str(self.book), 'Ein Titel by Mr X')
    
    def test_rating_model(self):
        self.assertEqual(self.review.book, self.book)  #testet foreignKey
        self.assertEqual(self.review.review_text, 'Test Review')
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(str(self.review), 'Review of Ein Titel by Mr X')
        





