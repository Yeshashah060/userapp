from django.contrib import admin
from.models import usermodel 
from django import forms

# Register your models here.
class SignupForm(forms.ModelForm):
	class Meta:
		model=usermodel
		fields= '__all__'



class LoginForm(forms.ModelForm):
	class Meta:
		model=usermodel
		fields= ['username' , 'password']



