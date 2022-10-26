from email import message
from email.headerregistry import Address
from django.db import models
from datetime import datetime
# from django.db.models import signals
# from django.dispatch import receiver

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=50)
    Roll_no = models.IntegerField()
    class_no = models.IntegerField()
    Address = models.CharField(max_length=70)
    
    def __str__(self):
        return str(self.id)

class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    ephn = models.IntegerField()
    esalary = models.IntegerField()

    def __str__(self):
        return str(self.ename) 

class EmployeeSalary(models.Model):
    basic = models.CharField(max_length=50)
    hra = models.IntegerField()
    special_allowance = models.IntegerField()
    pf_deduction = models.IntegerField()
    income_tax = models.IntegerField()
    proffesional_tax = models.IntegerField()
    convenience = models.IntegerField()
    lta = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='EmployeeSalary',null=True, blank=True)

    def __str__(self):
        return str(self.basic)

class Employees(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=50)
    class meta:
        db_table = 'employees'
   
class Demoapp(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return str(self.name)

# @receiver(signals.post_save,sender=Product)
# def create_product(sender,instance,created,**kwargs):
#     print('save method is called')

# @receiver(signals.pre_save,sender=Product)
# def check_product_description(sender,instance,**kwargs):
#     if not instance.description:
#         instance.description='this is default description'

class Profile(models.Model):
    name = models.CharField(max_length=50)
    email  = models.EmailField(max_length=50)
    bio = models.CharField(max_length=70)
    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name


class QuizModel(models.Model):
    question = models.CharField(max_length = 250)
    option1 = models.CharField(max_length=250)
    option2 = models.CharField(max_length=250)
    option3 = models.CharField(max_length=250)
    option4 = models.CharField(max_length=250)
    ans = models.CharField(max_length=250)
    def __str__(self):
        return self.question

class CrudUser(models.Model):
    name = models.CharField(max_length = 80)
    address = models.CharField(max_length = 50)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Emp(models.Model):
    Empcode = models.IntegerField()
    Name = models.CharField(max_length=50)
    DOBirth = models.DateField(max_length=50)
    DOJoining = models.DateField(max_length=50)
    DOAnniversary = models.DateField(max_length=50)
    Email = models.EmailField(max_length=50)

    def __str__(self):
        return self.Name
    
  





