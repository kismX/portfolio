from django.urls import path
from .views import SignUpView, SessionKexExample

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('session/', SessionKexExample.as_view()),

]