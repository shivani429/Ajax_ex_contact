from django.contrib import admin
from django.urls import path
from . import views
from demoapp.views import *
urlpatterns = [

    path('', views.hello, name='hello'),
    path('signup', SignUpView.as_view(), name='signupview'),
    path('validate_username', views.validate_username, name='validate_username'),
    path('contactform', views.contactform, name='contactform'),

]
