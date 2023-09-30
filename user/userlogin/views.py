from django.shortcuts import render,redirect
from.models import usermodel
from.forms import SignupForm
from.forms import LoginForm
# Create your views here.


def Signuppage(request):
	if request.method == "POST":
		signup_form = SignupForm(request.POST)
		if signup_form.is_valid():
			signup_form.save()
		return redirect(loginpage)

	signup_form = SignupForm()
	signup = usermodel.objects.all()
	context = {'signup_form':signup_form, 'signup':signup}
	return render(request, 'signup.html', context)


def loginpage(request):
	

	login_form = LoginForm()
	login = usermodel.objects.all()
	context = {'login_form':login_form, 'login':login}
	return render(request, 'login.html', context)