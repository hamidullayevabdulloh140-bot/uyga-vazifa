from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    desc = models.TextField()
    image = models.FileField(upload_to='image/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title 

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title 
