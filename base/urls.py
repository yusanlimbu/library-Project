
from django.urls import path
from .views import book_list,add_book,update_book,update_student,delete_book,delete_student,home_view,admin_login,issue_book,return_book
from . import views
from base import views

app_name = 'base'

urlpatterns = [

    
    #books
    path('book_list/', book_list, name='book_list'),
    path('add_book/', add_book, name='add_book'),
    path('update_book/<str:pk>', update_book, name='update_book'),
    path('delete_book/<str:pk>', delete_book, name='delete_book'),


    #Student
    path('student_list/', views.student_list, name='student_list'),
    path('update_student/<str:pk>', update_student, name='update_student'),
    path('delete_student/<str:pk>', delete_student, name='delete_student'),
    # path('student/<int:pk>/update',views.StudentUpdateView.as_view(),name = 'student-update'),


    #issued and return
    path('issue_book/', views.issue_book, name='issue_book'),
    path('issue_detail/', views.issue_detail, name='issue_detail'),
    path('return_book/<int:issue_id>/', return_book, name='return_book'),


    #excel import
    path('import/', views.upload, name='import'),


    #login
    path("admin_login/", views.admin_login, name="admin_login"),
    path("student_login/", views.student_login, name="student_login"),
    path("logout/", views.Logout_User, name="logout"),
    path('', home_view, name='index'),

]