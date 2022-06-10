from django.db import models

# Create your models here.

class Book(models.Model):
    Book_Name = models.CharField(max_length=100)
    Book_Author = models.CharField(max_length=100)
    Book_Price = models.CharField(max_length=10)


    def __str__(self):
        return self.Book_Name
