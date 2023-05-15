from django.forms import ModelForm
from .models import Book,Student


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
