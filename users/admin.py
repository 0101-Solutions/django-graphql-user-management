from django.contrib import admin

from users.models import ExtendedUser

# Register your models here.

admin.site.register(ExtendedUser)