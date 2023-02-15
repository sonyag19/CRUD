from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"  #[eid,ename,econtact,eemail]


class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields="__all__"

class Itemform(forms.Form):
    iname=forms.CharField(max_length=20)
    price=forms.IntegerField()
    des=forms.CharField(max_length=50)
    image=forms.FileField()