from django.db import models


# Create your models here.




class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    total_copies = models.PositiveIntegerField(default=0)
    available_copies = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class Student(models.Model):
    student_id = models.CharField(max_length=64,primary_key=True, unique=True)
    name = models.CharField(max_length=64, default='')  
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=128)
    course = models.CharField(max_length=10)
    batch = models.CharField(max_length=10)  
    phone_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return str(self.name) 
    

    

from datetime import datetime,timedelta


def expiry():
    return datetime.today() + timedelta(days=1)

class Issue(models.Model):
    book = models.ForeignKey(Book,null=True, on_delete=models.PROTECT)
    student = models.ForeignKey(Student,null=True, on_delete=models.PROTECT)
    issue_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(default=expiry)
    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=[('issued', 'Issued'), ('returned', 'Returned')], default='issued')

    def __str__(self):
        return f'{self.student} issued {self.book}'
