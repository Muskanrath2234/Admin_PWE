from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *


def home(request):
    return render(request,'home.html') 


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                auth_login(request, user)
                messages.info(request, f'{username}, You are logged in.')
                return redirect('home')  # Replace 'home' with the actual name of your home view
            else:
                messages.info(request, 'You do not have permission to access this page.')
                return redirect('admin_login')
        else:
            messages.info(request, 'Wrong password or username')
            return redirect('admin_login')
    return render(request, 'login.html')



def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account is created.')
            return redirect('home')
        else:
            context = {'form': form}
            messages.info(request, 'Invalid credentials')
            return render(request, 'register.html', context)

    context = {'form': form}
    return render(request, 'register.html', context)

def view_all_users(request):
   users = User.objects.all()
   return render(request,'view_all_users.html',{'users':users})

def user_logout(request):
    logout(request)
    return redirect('admin_login')


@login_required
def view_profile(request):
    user = request.user
    return render(request, 'view_profile.html', {'user': user})


@login_required(login_url='admin_login')
def editprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated.')
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form': form}
    return render(request, 'editprofile.html', context)





def user_logout(request):
    logout(request)
    return redirect('admin_login')