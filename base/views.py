from django.shortcuts import render, redirect

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import BookForm,StudentForm

from django.urls import reverse_lazy




def book_list(request):
    books = Book.objects.all()
    return render(request, 'base/book_list.html', {'books':books} )

def student_list(request):
    students = Student.objects.all()
    return render(request, 'base/student_list.html', {'students':students} )

# def add_book(request):
#     form = BookForm()
#     if request.method == 'POST':
#         #print('Printing POST:',request.POST)
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('base:book_list')

#     context = {'form':form}
#     return render(request,'base/add_book.html', context)


def add_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)  # Create a book instance but don't save it yet
            
            # Perform additional validation
            isbn = form.cleaned_data['isbn']
            if len(isbn) != 10:
                form.add_error('isbn', 'ISBN must be exactly 10 characters long.')


            if book.total_copies < 0:
                form.add_error('total_copies', 'Total copies must be a non-negative number.')
            
            if book.available_copies < 0:
                form.add_error('available_copies', 'Available copies must be a non-negative number.')
            
            if book.available_copies > book.total_copies:
                form.add_error('available_copies', 'Available copies cannot exceed total copies.')

            if book.total_copies != book.available_copies:
                form.add_error('total_copies', 'Total copies must equal available copies.')

            if form.errors:
                # If there are any validation errors, render the form with errors
                context = {'form': form}
                return render(request, 'base/add_book.html', context)
            
            # All validation checks passed, save the book
            book.save()
            
            return redirect('base:book_list')

    context = {'form': form}
    return render(request, 'base/add_book.html', context)



# def update_book(request,pk):

#     book = Book.objects.get(pk=pk)
#     form = BookForm(instance=book)
#     if request.method == 'POST':
#         #print('Printing POST:',request.POST)
#         form = BookForm(request.POST, instance = book)
#         if form.is_valid():
#             form.save()
#             return redirect('base:book_list')

#     context = {'form':form}
#     return render(request,'base/add_book.html', context)


def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            updated_book = form.save(commit=False)  # Create a book instance but don't save it yet
            
            # Perform additional validation
            if updated_book.total_copies < 0:
                form.add_error('total_copies', 'Total copies must be a non-negative number.')
            
            if updated_book.available_copies < 0:
                form.add_error('available_copies', 'Available copies must be a non-negative number.')
            
            if updated_book.available_copies > updated_book.total_copies:
                form.add_error('available_copies', 'Available copies cannot exceed total copies.')

            if updated_book.total_copies != updated_book.available_copies:
                form.add_error('total_copies', 'Total copies must equal available copies.')

            if form.errors:
                # If there are any validation errors, render the form with errors
                context = {'form': form}
                return render(request, 'base/add_book.html', context)
            
            # All validation checks passed, save the updated book
            updated_book.save()
            
            return redirect('base:book_list')

    context = {'form': form}
    return render(request, 'base/add_book.html', context)




def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponseRedirect(reverse('base:book_list'))










def update_student(request,pk):

    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            return redirect('base:student_list')

    context = {'form':form}
    return render(request,'base/student_update.html', context)



# def delete_student(student_id):
#     student = Student.objects.get(student_id=student_id)
#     if student:
#         student.delete()
#     return student

def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return HttpResponseRedirect(reverse('base:student_list'))
    # return HttpResponseRedirect(reverse('base:student_list'))




def home_view(request):
    return render(request,'base/index.html')











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




