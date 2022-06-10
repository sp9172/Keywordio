from django.db import models

# Create your models here.

class Book(models.Model):
    BookName = models.CharField(max_length=100)
    BookAuthorname = models.CharField(max_length=100)
    BookPrice = models.CharField(max_length=10)


    def __str__(self):
        return self.Book_Name
