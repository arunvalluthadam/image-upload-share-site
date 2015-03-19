from django import forms
from django.contrib.auth.models import User
from .models import *

class RegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','username','email')
		widgets = {
			'first_name': forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter First Name"}),
			'last_name': forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Last Name"}),
			'username': forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Username"}),
			# 'email': forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Email"}),
			# 'password1': forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Password"}),
			# 'password2': forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Password"}),
		}


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Email ID",'style':'margin-bottom:20px;',"name":"username"}),
                                label=u'')
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={"class":"form-control",'placeholder':"Password",'type':'password','style':'margin-bottom:20px;','name':'password'}), required=True)


class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('image',)
		widgets = {
			'image': forms.FileInput(attrs={"name":"image_src", "id":"image_src", "type":"file"}),
		}
