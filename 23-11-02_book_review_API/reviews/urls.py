from django.urls import path
from .views import BookListAPIView, BookDetailAPIView, ReviewListAPIView, ReviewDetailAPIView

urlpatterns = [
    path('book/<int:pk>/', BookDetailAPIView.as_view(), name='book_detail'),
    path('book/', BookListAPIView.as_view(), name='book_list'),
    path('review/<int:pk>/', ReviewDetailAPIView.as_view(), name='review_detail'),
    path('review/', ReviewListAPIView.as_view(), name='review_list'),
]