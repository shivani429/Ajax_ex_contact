from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from itsdangerous import Serializer
from .models import Emp,Employee,Blog,QuizModel,Student,EmployeeSalary,Employees,Profile,CrudUser    
from demoapp.forms import EmployeeForm, LoginForm, QuizModelForm,StudentForm,CreateUserForm,PhotoForm,ContactForm,EmpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
from django.views.generic.edit import CreateView,FormView
from django.views.generic import ListView,View
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
# from .models import Blog

# def mul(request):
#     if request.method =='POST':
#         val1 = int(request.POST['fn'])
#         val2 = int(request.POST['sn'])
#         res = val1 * val2
#     return render(request,'result.html',{'result':res})
    

def home(request):
    return render(request,'home.html',{'name':'Django'})

def home(request):
    post = Blog.objects.all()
    return render(request,'home.html',{'post':post})

# def indexView(request):
#     return render(request,'index.html')

# def dashboardView(request):
#     return render(request,'dashboard.html')

def home(request):
       return render(request, 'home.html')   

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             return HttpResponse(request,'login.html',{'form':form})
#     else:
#         return render(request,'login1.html')
       

# Student Functions
@login_required(login_url='login')
def student_list(request):
    student_list = Student.objects.all().order_by()
    d = {'student_list': student_list}
    return render(request,'index.html',d)
    
def delete_student(request,id):
    stu = Student.objects.get(id=id).delete()
    return redirect('student_list')

def update_student(request, id):
    stu = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        
        if form.is_valid():
            form .save()
         
        # Name = request.POST.get('name')
        # roll_no_=request.POST.get('Roll_no')
        # class_no_ = request.POST.get('class_no')
        # address = request.POST.get('Address')
        # print(Name)
        # print(roll_no_)
        # print(class_no_)
        # print(address)
        # # a = Student.objects.filter(Roll_no=roll_no_)
        # stu.Roll_no = roll_no_
        # stu.name = Name
        # stu.class_no = class_no_
        # stu.Address = address
        # stu.save()
      
        return redirect('student_list',)
    else:
    
        d = {'stu': stu}
        return render(request,'update.html',d)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            name = form.cleaned_data['name']
            roll_no = form.cleaned_data['roll_no']
            class_no = form.cleaned_data['class_no']
            address = form.cleaned_data['address']
            instance = Student(name=name, Roll_no=roll_no, class_no=class_no, Address=address)
            instance.save()
        # Name = request.POST.get('name')
        # roll_no_=request.POST.get('Roll_no')
        # class_no_ = request.POST.get('class_no')
        # address = request.POST.get('Address')
        # print(Name)
        # print(roll_no_)
        # print(class_no_)
        # print(address)
        # Student.objects.create(Roll_no=roll_no_,name=Name,class_no=class_no_,Address=address)
        return redirect('student_list')
    else:
        form = StudentForm()
        return render(request, 'update.html', {"form": form})


# Employee Functions
@login_required(login_url='login')
def employee_list(request):
    employee_list = Employee.objects.all()
    e = {'employee_list':employee_list}
    return render(request,'employee.html', e)

def delete_employee(request,id):
    em = Employee.objects.get(id=id).delete()
    return redirect('employee_list')

def edit_employee(request,id):
    em = Employee.objects.get(id=id)
    if request.method=='POST':
        eid_ = request.POST.get('eid')
        ename_ = request.POST.get('ename')
        ephn_ = request.POST.get('ephn')
        esalary_ = request.POST.get('esalary')
        print('eid_')
        print('ename_')
        print('ephn_')
        print('esalary_')
        em.eid = eid_
        em.ename = ename_
        em.ephn = ephn_
        em.esalary = esalary_
        em.save()
        return redirect('employee_list')
    else:
        e = {'em':em}
        return render(request,'edit.html',e)

def add_employee(request):
    if request.method=='POST':
        eid_ = request.POST.get('eid')
        ename_ = request.POST.get('ename')
        ephn_ = request.POST.get('ephn')
        esalary_ = request.POST.get('esalary')
        print('eid_')
        print('ename_')
        print('ephn_')
        print('esalary_')
        Employee.objects.create(eid = eid_, ename = ename_, ephn = ephn_, esalary = esalary_)
        return redirect('employee_list')
    else:
        return render(request,'edit.html')

#task1 using foreign key
def salary_list(request):
    salary_list = EmployeeSalary.objects.all()
    s = {'salary_list':salary_list}
    return render(request,'salary.html',s)

def deletesalary(request,id):
    salary = EmployeeSalary.objects.get(id=id).delete()
    return redirect('salary_list')

def update_salary(request,id):
    salary = EmployeeSalary.objects.get(id=id)
    if request.method == 'POST':
        basic_ = request.POST.get('basic')
        hra_ = request.POST.get('hra')
        special_allowance_ = request.POST.get('special_allowance')
        pf_deduction_ = request.POST.get('pf_deduction')
        income_tax_ = request.POST.get('income_tax')
        proffesional_tax_ = request.POST.get('proffesional_tax')
        convenience_ = request.POST.get('convenience')
        lta_ = request.POST.get('lta')
        employee_ = request.POSt.get('employee')
        print('basic_')
        print('hra_')
        print('special_allowance_')
        print('pf_deduction_')
        print('income_tax_')
        print('proffesional_tax_')
        print('convenience_')
        print('lta_')
        print('employee')
        salary.basic = basic_
        salary.hra = hra_
        salary.special_allowance = special_allowance_
        salary.pf_deduction = pf_deduction_
        salary.income_tax = income_tax_
        salary.proffesional_tax = proffesional_tax_
        salary.convenience = convenience_
        salary.lta = lta_
        salary.employee = employee_
        salary.save()
        return redirect('salary_list')
    else:
        a = {'salary':salary}
        return render(request,'update1.html',a)

def addcontent(request):
    employee_list = Employee.objects.all()
    if request.method == 'POST':
        basic_ = request.POST.get('basic')
        hra_ = request.POST.get('hra')
        special_allowance_ = request.POST.get('special_allowance')
        pf_deduction_ = request.POST.get('pf_deduction')
        income_tax_ = request.POST.get('income_tax')
        proffesional_tax_ = request.POST.get('proffesional_tax')
        convenience_ = request.POST.get('convenience')
        lta_ = request.POST.get('lta')
        employee = request.POST.get('employee')
        
        EmployeeSalary.objects.create(basic=basic_, hra=hra_, 
        special_allowance=special_allowance_, pf_deduction=pf_deduction_, 
        income_tax=income_tax_, proffesional_tax=proffesional_tax_, convenience=convenience_, 
        lta=lta_,employee_id=employee)
        return redirect('salary_list')
    else:
        return render(request,'update1.html',{'employee_list':employee_list})

#CRUD operation using model form
def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('show')
            except:
                pass
    else:
        form = EmployeeForm()
        return render(request,'index2.html',{'form':form})

def show(request):
    employee = Employees.objects.all()
    return render(request,'show.html',{'employee':employee})

def edit(request,id):
    employee = Employees.objects.get(id=id)
    return render(request,'edit2.html',{'employee':employee})

def update(request,id):
    employee = Employees.objects.get(id=id).update()
    form = EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('show')
    return render(request,'edit2.html',{'employee':employee})

def delete(request,id):
    employee = Employees.objects.get(id=id)
    employee.delete()
    return redirect('show')

#Authentication 
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Incorrect Username or Password')
        return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

def registerpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('user')
            messages.success(request,'Account created for '+ 'user') 
            return redirect('login')

    context = {'form':form}
    return render(request,'register1.html',context)

#javascript validation
def insert(request):
    return render(request,'insert.html')

#AJAX example
def profile(request):
    return render(request,'profile.html')

def getprofile(request):
    profile = Profile.objects.all()
    return JsonResponse({'profile':list(profile.values())})

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        bio = request.POST['bio']
        new_user = Profile(name=name, email=email, bio=bio)
        new_user.save()
        return HttpResponse('new data created successfully')

#AJAX example
def photo_view(request):
    form = PhotoForm(request.POST or None, request.FILES or None)
    data = {}
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data["name"] = form.cleaned_data.get("name")
            data["status"] = 'ok'
            return JsonResponse(data)
    context = {'form':form}
    return render(request,'main.html',context)

#AJAX example
def hello(request):
    return render(request,'hello.html')

class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('hello')
    def form_valid(self,form):
        valid = super().form_valid(form)
        login(self.request,self.object)
        return valid
def validate_username(request):
    username = request.GET.get('username',None)
    response = {
        'is_taken':User.objects.filter(username__iexact = username).exists()
    }
    return JsonResponse(response)

def contactform(request):
    form = ContactForm()
    if request.method == "POST" and request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return JsonResponse({"name":name}, status = 200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors':errors}, status = 400)
    return render(request,'contact.html',{'form':form})

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    def form_valid(self,form):
        name = form.changed_data['name']
        form.save()
        return JsonResponse({'name':name},status = 200)
    def form_invalid(self,form):
        errors = form.errors.as_json()
        return JsonResponse({'errors':errors},status = 400)
    
#CRUD using AJAX
class crudview(ListView):
    model = CrudUser
    template_name = "crud.html"
    context_object_name = 'users'

class CreateCrudUser(View):
    def get(self,request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age',None)
        obj = CrudUser.objects.create(name=name1, address = address1, age = age1)
        user = {'id':obj.id, 'name':obj.name, 'address':obj.address, 'age':obj.age}
        data = {'user':user}
        return JsonResponse(data)
class UpdateCrudUser(View):
    def get(self,request):
        id1 = request.GET.get('id',None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age',None)
        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        user = {'id':obj.id, 'name':obj.name, 'address':obj.address, 'age':obj.age}
        data = {'user':user}
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
    
#QuizForm    
def hom(request):
    if request.method == "POST":
        questions=QuizModel.objects.all()
        score=0
        correct=0
        wrong=0
        total=0
        for q in questions:
            total+=1
            if q.ans == request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
        context = {
            'score':f'{score}/{total}',
            'correct':correct,
            'wrong':wrong,
            'total':total
        }
        return render(request,'res.html',context)
    else:
        questions = QuizModel.objects.all()
        context = {'questions':questions}
        return render(request,'hom.html',context)  
    
def addquestion(request):
    form = QuizModelForm()
    if request.method == 'POST':
        form = QuizModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('addquestion')
    context={'form':form}
    return render(request,'addqns.html',context)

#task3
def email(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('empdata')
            except:
                pass
    else:
        form = EmpForm()
    return render(request, 'email.html', {"form": form})


def empdata(request):
    object = Emp.objects.all()
    return render(request, 'empdata.html', {'object': object})


def update_data(request, id):
    object = Emp.objects.get(id=id)
    if request.POST:
        if object:
            object.Empcode = request.POST['Empcode']
            object.Name =request.POST['Name']
            object.DOBirth =request.POST['DOBirth']
            object.DOJoining = request.POST['DOJoining']
            object.DOAnniversary = request.POST['DOAnniversary']
            object.Email = request.POST['Email']
            object.save()
        return redirect('empdata')
    return render(request, 'editdata.html', {'object': object})


def delete_data(request, id):
    object = Emp.objects.get(id=id)
    object.delete()
    return redirect('empdata')

def data(request):
    return redirect('edata')

def edata(request):
    today_date = datetime.today().date()
    birthdays = Emp.objects.filter(DOBirth__day=today_date.day,DOBirth__month=today_date.month)
    joining = Emp.objects.filter(DOJoining__day=today_date.day,DOJoining__month=today_date.month)
    annversary = Emp.objects.filter(DOAnniversary__day=today_date.day,DOAnniversary__month=today_date.month)
    return render(request, 'data.html',{'birthdays':birthdays, 'joining':joining, 'annversary':annversary})

def query(request):
    return redirect('mail')

def mail(request):
#     subject = 'hello'
#     message = 'hi'
#     sendfrom = settings.EMAIL_HOST_USER
#     toaddress = ['s10828556@gmail.com',]
#     send_mail(subject,message,sendfrom,toaddress)
    return render(request,'message.html')



