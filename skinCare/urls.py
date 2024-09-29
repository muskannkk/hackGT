from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', include('skinCare.urls')),
    path('homePage/', views.homePage, name='homePage'),
    path('calendar/', views.calendar, name='calendar'),
    path('days/<str:month>/<int:day>/', views.days, name='days'),
    path('login/', views.login, name='login'),
    path('monthOverview/', views.monthOverview, name='monthOverview'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)