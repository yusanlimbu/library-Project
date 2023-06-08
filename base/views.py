from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import BookForm,StudentForm,IssueForm

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


def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return HttpResponseRedirect(reverse('base:student_list'))



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







from datetime import date

def issue_detail(request):
    today = date.today()
    issues = Issue.objects.all()

    for issue in issues:
        if issue.expiry_date < today and issue.status == 'issued':
            # Calculate the fine
            days_overdue = (today - issue.expiry_date).days
            fine = days_overdue * 10  
            issue.fine = fine
            issue.save()
    return render(request, 'base/issue/issue_detail.html', {'issues': issues})





def issue_book(request):
    form = IssueForm()
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']

            if book.available_copies > 0:
                book.available_copies -= 1
                book.save()

                form.save()
                return redirect('base:issue_detail')
            else:
                form.add_error('book', 'This book is currently not available for issuance.')

    context = {'form': form}
    return render(request, 'base/issue/issue_book.html', context)




def return_book(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.status = 'returned'
    issue.fine = 0
    issue.save()

    book = issue.book
    book.available_copies += 1
    book.save()

    messages.success(request, 'Book returned successfully.')

    return redirect('base:issue_detail')












def home_view(request):
    return render(request,'base/index.html')




from django.contrib.auth import authenticate, login, logout

# def admin_login(request):
#     if request.method == "POST":
#         email= request.POST['username']
#         password = request.POST['password']
#         user = authenticate(email=email, password=password)

#         if user is not None:
#             login(request, user)
#             if request.user.is_superuser:
#                 return redirect("base:book_list")
#             else:
#                 return HttpResponse("You are not an admin.")
#         else:
#             alert = True
#             return render(request, "base/accounts/adminlogin.html", {'alert':alert})
#     return render(request, "base/accounts/adminlogin.html")




def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("base:book_list")
            else:
                return HttpResponse("You are not an admin.")
        else:
            alert = True
            return render(request, "base/accounts/adminlogin.html", {'alert':alert})
    return render(request, "base/accounts/adminlogin.html")






def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("You are not a student!!")
            else:
                return redirect("/profile")
        else:
            alert = True
            return render(request, "student_login.html", {'alert':alert})
    return render(request, "student_login.html")



def Logout(request):
    logout(request)
    return redirect ("/")