import http
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from . forms import BookForms,Loginform,SingUpForm
from . models import Book
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group,Permission
# Create your views here.

def book_form(request,id=0):

    if request.method =="GET":
        if id==0:
            form=BookForms() 
        else:
            bk=Book.objects.get(pk=id)
            form=BookForms(instance=bk)
        return render(request,'bookadd.html',{'form':form})
    else:
        if id==0:

            form=BookForms(request.POST)
        else:
            bk=Book.objects.get(pk=id)
            form=BookForms(request.POST,instance=bk)


        if form.is_valid():
            form.save()

       
        return redirect('BOOKLIST')

def index(request):
    return render(request,'main.html')

def book_list(request):
    if request.user.is_authenticated:
        context={
            'booklist':Book.objects.all()
        }
        # print(context)
        return render(request,'booklist.html',context)
    else:
        return HttpResponseRedirect('/bookform')

def book_delete(request,id):
    bk=Book.objects.get(pk=id)
    bk.delete()
    return redirect('BOOKLIST')

def user_sing(request):
    if request.method=="POST":
        
        form=SingUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SingUpForm() 
    return render(request,'signup.html',{'form':form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = Loginform(request=request,data=request.POST)
            if form.is_valid():
                unm = form.cleaned_data['username']
                pwd = form.cleaned_data['password']
                user=authenticate(username=unm,password=pwd)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/booklist')
        else:
            form = Loginform()
        
        return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/booklist')

def lUSER_ogout(request):
    logout(request)
    return HttpResponseRedirect('/')



