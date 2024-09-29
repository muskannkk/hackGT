from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Day(models.Model):
    date = models.DateField()
    #dailyPicture = models.ImageField(upload_to='day/')
    notes = models.TextField()
    dayProducts = models.TextField()
    nightProducts = models.TextField()
    diet = models.TextField()

class MonthOverview(models.Model):
    janNotes = models.TextField()
    febNotes = models.TextField()
    marNotes = models.TextField()
    aprNotes = models.TextField()
    mayNotes = models.TextField()
    junNotes = models.TextField()
    julNotes = models.TextField()
    augNotes = models.TextField()
    sepNotes = models.TextField()
    octNotes = models.TextField()
    novNotes = models.TextField()
    decNotes = models.TextField()

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   #profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
   days = models.ManyToManyField(Day, blank=True)
   januaryNotes = models.TextField(default="")
   februaryNotes = models.TextField(default="")
   marchNotes = models.TextField(default="")
   aprilNotes = models.TextField(default="")
   mayNotes = models.TextField(default="")
   juneNotes = models.TextField(default="")
   julyNotes = models.TextField(default="")
   augustNotes = models.TextField(default="")
   septemberNotes = models.TextField(default="")
   octoberNotes = models.TextField(default="")
   novemberNotes = models.TextField(default="")
   decemberNotes = models.TextField(default="")

   def __str__(self):
       return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
   if created:
       Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
   instance.profile.save()
