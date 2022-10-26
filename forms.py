from dataclasses import fields
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__' 

