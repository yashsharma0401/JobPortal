from django.contrib import admin
from .models import Job, Applicants, Selected
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms


admin.site.register(Job)
admin.site.register(Selected)
admin.site.register(Applicants)
