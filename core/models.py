from django.db import models

# Create your models here.


class Data(models.Model):
    # sentiment = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    word = models.TextField(max_length=100)
    count = models.IntegerField()

class Movie(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    
class theatre(models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=100)
    
class Actor(models.Model):
    name = models.CharField(max_length=100)

class Book_Author(models.Model):
    name = models.CharField(max_length=100)

class Library(models.Model):
    name = models.CharField(max_length=100)

class Movie_Actor(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    name = models.CharField(max_length=100)
 
class Payment(models.Model):
    name = models.CharField(max_length=100)
 
class Cart(models.Model):
    name = models.CharField(max_length=100)
    
class Movie_Author(models.Model):
    name = models.ForeignKey(Author, on_delete=models.CASCADE)
    mv = models.ForeignKey(Movie, on_delete=models.CASCADE)
