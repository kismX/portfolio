from django.urls import reverse_lazy      # rechericheren
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

    # def get(self, request, *args, **kwargs):
    #     print('BLA', self.kwargs.get('pk'))             # hier kann man im terminal die primary key des posts ausgeben lassen (schau unter der haube von def get im django und dann ...)
    #     return super().get(request, *args, **kwargs)

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['title', 'body']
    # success_url = reverse_lazy('home')


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')