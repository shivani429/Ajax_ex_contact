from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Contact    
from demoapp.forms import ContactForm
from django.contrib.auth.forms import UserCreationForm

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
