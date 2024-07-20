from django import forms
from .models import *

class MyForm(forms.ModelForm):
     class Meta:
         model = Contact_Messages
         fields = '__all__'

class adminform(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField()        


class serviceForm(forms.ModelForm):
    class Meta:
        model=Services
        fields='__all__'                     