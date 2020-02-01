from django.db import models
from django.contrib.auth.models import User
import DevelopersToolkit.settings as settings
from django.core.files.storage import FileSystemStorage
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Role(models.Model):
    ROLE_CHOICES = (
        (1, 'founder'),
        (2, 'supervisor'),
        (3, 'developer'),
        (4, 'default'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    avatar = models.ImageField(upload_to='user_avatars/')
    name = models.CharField(max_length=24, blank=False, null=True)
    title = models.CharField(max_length=60, blank=False)
    education = models.CharField(max_length=100, blank=False)
    mail = models.EmailField(max_length=255, blank=False)
    github = models.URLField(max_length=200, blank=False)
    linkedin = models.URLField(max_length=200, blank=False)
    bio = models.TextField(max_length=500, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
