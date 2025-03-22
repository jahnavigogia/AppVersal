from django.contrib import admin
from django.contrib import admin
from django import forms
from django.db import models
from .models import User

#
# class UserAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.DateField: {'widget': forms.TextInput(attrs={'type': 'text'})},  # Removes date picker
#     }

admin.site.register(User)
