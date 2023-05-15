
from django.urls import path
from .views import book_list,add_book,update_book,update_student,delete_book,delete_student,home_view
from . import views
from base import views

app_name = 'base'

urlpatterns = [

    
    #books
    path('', book_list, name='book_list'),
    path('add_book/', add_book, name='add_book'),
    path('update_book/<str:pk>', update_book, name='update_book'),
    path('delete_book/<str:pk>', delete_book, name='delete_book'),


    #Student
    path('student_list/', views.student_list, name='student_list'),
    path('update_student/<str:pk>', update_student, name='update_student'),
    path('delete_student/<str:pk>', delete_student, name='delete_student'),
    # path('student/<int:pk>/update',views.StudentUpdateView.as_view(),name = 'student-update'),


    #excel import
    path('import/', views.upload, name='import'),
    path('home/', home_view, name='index'),
]