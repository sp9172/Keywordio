from django.shortcuts import redirect, render
from . forms import BookForms
from . models import Book

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


    context={
        'booklist':Book.objects.all()
    }
    # print(context)
    return render(request,'booklist.html',context)

def book_delete(request,id):
    bk=Book.objects.get(pk=id)
    bk.delete()
    return redirect('BOOKLIST')
