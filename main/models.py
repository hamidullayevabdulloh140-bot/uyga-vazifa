from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

