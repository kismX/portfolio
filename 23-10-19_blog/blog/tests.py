from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):                                 # wichtig , das setup.. mach es dir kla, das createt einen testuser und einen testpostobject
        cls.user = get_user_model().objects.create_user(
            username="testuser", 
            email="test@email.com",
            password="secret"
        )
    
        cls.post = Post.objects.create(
            title="A good title",
            body="Nice Body content",
            author=cls.user,
        )
    
    # def test_post_model(self):
    #     self.assertEqual(self.post.title, "A good title"),
    #     self.assertEqual(self.post.body, "Nice Body content"),
    #     self.assertEqual(self.post.author.username, "testuser"),
    #     self.assertEqual(str(self.post), "A good title"),
    #     self.assertEqual(self.post.get_absolute_url(), "/post/1/")                  # irgfendwie geht was nicht

    
    # def test_url_exists_at_correct_location_listview(self):
    #     response = self.client.get("/post/1/")
    #     self.assertEqual(response.status_code, 200)
    
    # def test_post_listview(self):
    #     response = self.client.get(reverse('home'))
    #     self.assertEqual(response.status_code,200)
    #     self.assertContains(response, "Nice Body content")
    #     self.assertTemplateUsed(response, "home.html")




## testing CreateView -läuft

    def test_post_createview(self):
        response = self.client.post(
            reverse('post_new'),
            {
                "title": "New Title",
                "body": "New Text",
                "author": self.user.id,
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New Title")
        self.assertEqual(Post.objects.last().body, "New Text")




## teste Updateview -läuft

    def test_post_updateview(self):
        response = self.client.post(
            reverse("post_edit", args="1"),
            {
                "title": "Update title",
                "body": "Update text",
            } 
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Update title")
        self.assertEqual(Post.objects.last().body, "Update text")




## teste DeleteView -läuft

    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)
        
        self.assertIsNone(Post.objects.last())    # wenn kein eintrag

