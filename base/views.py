from django.shortcuts import render

# Create your views here.



# from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.contrib import messages
from .models import *





# def book_list(request):
#     books = Book.objects.all()
#     context = {'books': books}
#     return render(request, 'index.html', context)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'base/book_list.html', {'books':books} )

def student_list(request):
    students = Student.objects.all()
    return render(request, 'base/student_list.html', {'students':students} )















# from django.shortcuts import render,redirect
# from openpyxl import load_workbook
# from .models import Student

# def upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         # Check that the file extension is .xlsx
#         if not myfile.name.endswith('.xlsx'):
#             return render(request, 'base/student_import.html', {'error': 'File must be in .xlsx format.'})
#     # else:
#         wb = load_workbook(filename=myfile, read_only=True)
#         ws = wb.active
#         for row in ws.iter_rows(min_row=2):
#             student = Student(
#                 student_id=row[0].value,
#                 name=row[1].value,
#                 email=row[2].value,
#                 password=row[3].value,
#                 course=row[4].value,
#                 batch=row[5].value,
#                 phone_number=row[6].value
#             )
#             student.save()
#         return render(request, 'base/student_import.html', {'message': 'File uploaded successfully.'})
        
#     return render(request, 'base/student_import.html')



# views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from openpyxl import load_workbook
from .models import Student

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        # Check that the file extension is .xlsx
        if not myfile.name.endswith('.xlsx'):
            return render(request, 'base/student_import.html', {'error': 'File must be in .xlsx format.'})
        wb = load_workbook(filename=myfile, read_only=True)
        ws = wb.active
        for row in ws.iter_rows(min_row=2):
            student = Student(
                student_id=row[0].value,
                name=row[1].value,
                email=row[2].value,
                password=row[3].value,
                course=row[4].value,
                batch=row[5].value,
                phone_number=row[6].value
            )
            student.save()
        # return redirect('student_list')
        return redirect(reverse('base:student_list'))
    return render(request, 'base/student_import.html')




