from multiprocessing.dummy.connection import Client
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Blog)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'Roll_no', 'class_no', 'Address')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'eid', 'ename' ,'ephn', 'esalary')

admin.site.register(EmployeeSalary)

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id','eid','ename','eemail','econtact')

admin.site.register(Demoapp)

admin.site.register(Profile)

admin.site.register(Photo)

admin.site.register(Contact)

admin.site.register(QuizModel)

@admin.register(CrudUser)
class CrudUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'age')

admin.site.register(Emp)


