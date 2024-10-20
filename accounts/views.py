from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from  django.contrib import messages


# Create your views here.
from django.urls import reverse

from accounts.forms import CustomUserCreationForm


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return  redirect("/")
            else:
                messages.add_message(request, messages.SUCCESS, "Entered data are Not true")
    else:
        return redirect("/")
    return render(request,"accounts/login.html")

@login_required
def user_logout(request):
        logout(request)
        return redirect("/")

def forget_password(request):
    pass


def signup(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/signup.html", {'form': form})