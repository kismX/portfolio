from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Book

class BookModelTest(TestCase):

    # zunächst createn wir einen testuser und ein test-bookobject
    @classmethod
    def setUpTestData(cls):                                 
        cls.user = get_user_model().objects.create_user(
            username="testuser", 
            email="test@email.com",
            password="secret"
        )
    
        cls.book = Book.objects.create(
            title="Mein Buch",
            author="Halodri Penner",
            description='gutes Buch',
            published_date='2015-12-01',
            price=20,
        )

    # Test , ob Testobject korrekt erstellt wurde
    def test_post_model(self):
        self.assertEqual(self.book.title, "Mein Buch"),
        self.assertEqual(self.book.author, "Halodri Penner"),
        self.assertEqual(self.book.description, "gutes Buch"),
        self.assertEqual(self.book.published_date, "2015-12-01"),
        self.assertEqual(self.book.price, 20)
        # self.assertEqual(str(self.post), "A good title"),
        # self.assertEqual(self.book.get_absolute_url(), "/post/1/")

    
    def test_book_retrieval(self):
        book_from_db = Book.objects.get(title="Mein Buch")
        print(f"Retrieval-Test: {book_from_db}")
        self.assertEqual(book_from_db, self.book)           

    def test_book_update(self):
         self.book.title = "An updated title"
         self.book.save()
         updated_book = Book.objects.get(title=self.book.title)
         print(f" Update-Test: {updated_book}")
         self.assertEqual(updated_book.title, "An updated title")

    def test_book_deletion(self):
        book_id = self.book.pk
        print(f"Delete-Test: {book_id}")
        self.book.delete()
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=book_id)
    

    def test_str_representation(self):
        print("Str-Representation-Test: ")
        self.assertEqual(str(self.book), 'Mein Buch')

    def test_book_get_absolute_url(self):
        # Assuming you've defined a get_absolute_url method on the Book model that returns "/book/1/"
        print("Absolute-URL-Test: ")
        self.assertEqual(self.book.get_absolute_url(), f'/book/{self.book.id}')