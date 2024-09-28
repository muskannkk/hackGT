from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def homePage(request):
    return render(request, 'skinCare/homePage.html')
def calendar(request):
    return render(request,'skinCare/calendar.html')
def days(request):
    return render(request,'skinCare/days.html')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('monthOverview')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request,'skinCare/login.html')

def monthOverview(request):
    return render(request, 'skinCare/monthOverview.html')
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request,'skinCare/signup.html')