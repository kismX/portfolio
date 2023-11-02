from django.db import models
from django.urls import reverse

# wir createn einen table mit nem title, dem author und nem body , wir vernetzen das model mit der database auth_user

class Post(models.Model):                           
    title = models.CharField(max_length=200)
    # es gibt eine database "auth_user" - schau mal bei sql datei - mit der wollen wir das verlinken (primary foreign key dings). auth.Users ist hier eine Class in django
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)  # on_delete sagt, wenn user nicht vorhanden, dann wird gelöscht oder so
    body = models.TextField()

    def __str__(self):                  # um im adminbereich den title zu sehen
        return self.title
    
    def get_absolute_url(self):
        print(reverse('post_detail', kwargs={"pk": self.pk}))    # zeigt in terminmal was die zeile macht
        return reverse('post_detail', kwargs={"pk": self.pk}) # recherchiere was genacu da geschieht
    


