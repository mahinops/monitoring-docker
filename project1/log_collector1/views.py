from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics


def index(request):
    return HttpResponse("Welcome to the Log Collector 1 Index Page!")


# New DRF View
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
