# from django.urls import path
# from . import views

# # app_name = 'base'

# urlpatterns = [
#     path('',views.base ,name='book_list'),
#     path(''),
#     # path('admin/', admin.site.urls),
#     # path('', views.book_list, name='book_list'),
#     # path('<int:book_id>/', views.book_detail, name='book_detail'),

#     # path('',views.DashboardHomeView.as_view(),name='home'),


#      # Category
#     # path('book',views.BookListView.as_view(),name = 'book-list'),
#     # path('book/create',views.BookCreateView.as_view(),name = 'book-create'),
#     # path('book/<int:pk>/update',views.BookUpdateView.as_view(),name = 'book-update'),
#     # path('book/<int:pk>/detail/',views.BookDetailView.as_view(),name = 'book-detail'),
#     # path('book/<int:pk>/delete/',views.BookDeleteView.as_view(),name = 'book-delete'),
# ]




from django.urls import path
from .views import book_list
from base import views

app_name = 'base'

urlpatterns = [
    path('', book_list, name='book_list'),
    path('import/', views.upload, name='import'),



    #Student
    path('student_list/', views.student_list, name='student_list'),

    # path('books/add/', add_book, name='add_book'),
    # path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    # path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
]