from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),
]