from django.contrib import admin

# Register your models here.

from .models import Book
admin.site.register(Book)


from .models import Student
admin.site.register(Student)


from .models import *
admin.site.register(Issue)