from django import forms
from Prac12.models import *
from django.forms.widgets import NumberInput

GENDER_CHOICES = [('M','Male'),('F','Female')]
STATUS_CHOICES = [('Administrator','Administrator'), ('Manager', 'Manager'),('Staff','Staff'),('Sale Rep','Sale Rep')]
BORN_CHOICE = [('North','ภาคเหนือ'),('Middle','ภาคกลาง'),('ภาคอีสาน','Northeast'),('ภาคใต้','South'),('ภาคตะวันออก','East')]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('empid', 'name', 'address', 'status', 'email', 'salary', 'gender', 'birthday','born', 'marries')
        widgets = {
            'empid': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'status': forms.Select(attrs={'class': 'form-control'}, choices=STATUS_CHOICES),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'Min': '5000'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=GENDER_CHOICES, ),
            'birthday': forms.NumberInput(attrs={'class': 'form-control', 'type': 'date'}),
            'born': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=BORN_CHOICE),
            'marries': forms.CheckboxInput(attrs={'checked': 'checked'})
        }