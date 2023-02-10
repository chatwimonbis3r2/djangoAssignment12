from django import forms
from App12.models import *


class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('goodsCategory', 'gid', 'name', 'brand', 'model', 'price', 'net', 'property')
        widgets = {
            'goodsCategory': forms.Select(attrs={'class': 'form-control'}),
            'gid': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'net': forms.NumberInput(attrs={'class': 'form-control'}),
            'property': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'goodsCategory': 'Category',
            'gid': 'ID',
            'name': 'Name',
            'brand': 'Brand',
            'model': 'Model',
            'price': 'Price',
            'net': 'Net',
            'property': 'Property',
        }

    def GoodsEditForm(self):
        self.fields['gid'].widget.attrs['readonly'] = True
        self.fields['gid'].labels = 'ID (Not Allowed To Edit)'


Gender_Choice = [('Male', 'Male'), ('Female', 'Female')]


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cid', 'name', 'surname', 'password', 'address', 'telephone', 'gender', 'carreer')
        widgets = {
            'cid': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=Gender_Choice),
            'carreer': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'cid': 'ID',
            'name': 'Name',
            'surname': 'Surname',
            'password': 'Password',
            'telephone': 'Telephone',
            'gender': 'Gender',
            'carreer': 'Carreer',
        }

    def CustomerEditForm(self):
        self.fields['cid'].widget.attrs['readonly'] = True
        self.fields['cid'].labels = 'ID (Not Allowed To Edit)'
