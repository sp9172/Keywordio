# from pyexpat import model
# from cProfile import label
import email
from django.utils.translation import gettext,gettext_lazy as _
# from attr import _Fields, field
# from pyexpat import model
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UsernameField
# from matplotlib import widgets
from . models import Book 
from django import forms

from django.contrib.auth.models import User
class BookForms(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'


class SingUpForm(UserCreationForm):
    password1: forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2: forms.CharField(label='Confirm password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta :
        model = User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.TextInput(attrs={'class':'form-control'}),
        }





class Loginform(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-cotrol'}))
    password=forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplate':'current-password','class':'form-cotrol'}))
