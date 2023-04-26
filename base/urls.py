
from django.urls import path
from .views import book_list,add_book,update_book
from base import views

app_name = 'base'

urlpatterns = [
    #books
    path('', book_list, name='book_list'),
    path('add_book/', add_book, name='add_book'),
    path('update_book/<str:pk>', update_book, name='update_book'),


    #excel import
    path('import/', views.upload, name='import'),



    #Student
    path('student_list/', views.student_list, name='student_list'),

    # path('books/add/', add_book, name='add_book'),
    # path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    # path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
]