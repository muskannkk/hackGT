from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User

from skinCare.models import Profile, Day


# Create your views here.
def homePage(request):
    return render(request, 'skinCare/homePage.html')
def calendar(request):
    days_in_month = list(range(1, 32))  # Adjust as needed for each month
    context = {
        'days_in_month': days_in_month,
    }
    return render(request, 'skinCare/calendar.html', context)
MONTHS = {
    'January': '01',
    'February': '02',
    'March': '03',
    'April': '04',
    'May': '05',
    'June': '06',
    'July': '07',
    'August': '08',
    'September': '09',
    'October': '10',
    'November': '11',
    'December': '12',
}

def days(request, month, day):
    # Ensure the user is authenticated
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        year = 2025
        if request.method == "POST":
            # Retrieve data from the POST request
            daytimeProducts = request.POST.get('textbox2', '')
            nighttimeProducts = request.POST.get('textbox3', '')
            dietToday = request.POST.get('textbox4', '')
            additionalNotes = request.POST.get('textbox5', '')

            month_numeric = MONTHS.get(month)
            if not month_numeric:
                return render(request, 'skinCare/error.html', {'error': 'Invalid month'})

            date = f"{year}-{month_numeric}-{str(day).zfill(2)}"  # Ensure you have a valid date string
            day_instance, created = Day.objects.get_or_create(date=date)

            day_instance.notes = additionalNotes
            day_instance.dayProducts = daytimeProducts
            day_instance.nightProducts = nighttimeProducts
            day_instance.diet = dietToday
            day_instance.save()

            # Associate the Day instance with the Profile
            profile.days.add(day_instance)

            return redirect('days', month=month, day=day)

        # Prepare context data to display in the template
        month_numeric = MONTHS.get(month)
        day_info = profile.days.filter(date=f"{year}-{month_numeric}-{str(day).zfill(2)}").first()

        context = {
            'month': month,
            'day': day,
            'day_info': day_info,
        }

        return render(request, 'skinCare/days.html', context)

    # If user is not authenticated, redirect or show an error
    return redirect('login')

def profile(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        return render(request, 'skinCare/profile.html', {'profile': profile})
    else:
        return redirect('login')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('calendar')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('signup')
    return render(request,'skinCare/login.html')

def monthOverview(request):
    return render(request, 'skinCare/monthOverview.html')
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
        except Exception as e:
            messages.error(request, str(e))
    return render(request,'skinCare/signup.html')