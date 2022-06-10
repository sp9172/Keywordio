
from django.urls import path

from . import views


urlpatterns = [
    path('',views.user_login,name="Homeindex"),
  
    path('bookform',views.book_form,name="BOOKfORM"),
    path('<int:id>',views.book_form,name="BOOKUPDATE"),
    path('booklist',views.book_list,name="BOOKLIST"),
    path('delete/<int:id>',views.book_delete,name="BOOKDELETE"),
    path('logout',views.lUSER_ogout,name="LOGOUT"),
    path('singup',views.user_sing,name="UserS")
    
]