from pyexpat import model

from attr import _Fields, field
from . models import Book 
from django import forms

class BookForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'