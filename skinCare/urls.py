from django.urls import path
from . import views

urlpatterns = [
    path('homePage/', views.homePage, name='homePage'),
    path('calendar/', views.calendar, name='calendar'),
    path('days/<str:month>/<int:day>/', views.days, name='days'),
    path('login/', views.login, name='login'),
    path('monthOverview/', views.monthOverview, name='monthOverview'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]
