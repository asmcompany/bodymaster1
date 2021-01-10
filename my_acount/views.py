from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from my_acount.forms import LoginForm, RegisterForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')


    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('user_name','کلمه عبور وارد شده نا درست است')

    context = {
        'login_form': login_form
    }


    return render(request, "acount/login.html", context)

def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        first_name= register_form.cleaned_data.get('first_name')
        last_name = register_form.cleaned_data.get('last_name')
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name, email=email, password=password)
        return redirect('/login')

    context = {
        'register_form': register_form
    }


    return render(request, "acount/register.html",context)