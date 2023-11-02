from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, DetailView, UpdateView
from .models import Book
from django.urls import reverse_lazy

from .mixins import UserRequiredMixin

#from django.views.generic.edit import CreateView

# Create your views here.


class BookListView(UserRequiredMixin, ListView):   # du kannst UserRequiredMixin auch einfügen COR ListView für authentifizierung, aber es ist schon in middleware integrierrt
    model = Book
    template_name = 'book_list.html'


class BookDetailView(UserRequiredMixin, DetailView):
    model = Book
    template_name = "book_detail.html"

class BookCreateView(UserRequiredMixin, CreateView):
    model = Book
    template_name = "book_create.html"
    fields = ["title", "author", "description", "published_date", "price"]
    success_url = reverse_lazy("book_list")

class BookUpdateView(UserRequiredMixin, UpdateView):
    model = Book
    template_name = "book_edit.html"
    fields = ["title", "author", "description", "published_date", "price"]
    success_url = reverse_lazy("book_list")

class BookDeleteView(UserRequiredMixin, DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = reverse_lazy("book_list")