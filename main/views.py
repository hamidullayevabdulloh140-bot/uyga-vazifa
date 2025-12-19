from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .models import Book, Author, Article, Post
from .serializers import ArticleSerializer, AuthorSerializer, BookSerializer, PostSerializer

class AuthorAPIView(ListCreateAPIView,GenericAPIView ):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookAPIView(ListCreateAPIView, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PostAPIView(ListCreateAPIView, GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ArticleAPIView(ListCreateAPIView, GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
