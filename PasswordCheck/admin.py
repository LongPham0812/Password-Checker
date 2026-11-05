"""
Admin configuration for the Password Checker app.
"""

from django.contrib import admin

from .models import Password

admin.site.register(Password)