from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'skinCare/homePage.html')
def calendar(request):
    return render(request,'skinCare/calendar.html')
def days(request):
    return render(request,'skinCare/days.html')
def login(request):
    return render(request,'skinCare/login.html')
def monthOverview(request):
    return render(request, 'skinCare/monthOverview.html')
def signup(request):
    return render(request,'skinCare/signup.html')