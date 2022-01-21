from django.shortcuts import render
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your views here.

class ExtendedUser(AbstractUser):

    email = models.EmailField(blank=False, verbose_name="email")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

