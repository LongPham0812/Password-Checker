"""
Views for the Password Checker app. This file contains code to display the different pages of the app.
"""

from django.shortcuts import render, redirect
from .models import Password

def index(request):
    """Loads the home page"""
    Password.objects.all().delete()
    return render(request, 'PasswordCheck/index.html')

def empty_result():
    """Returns an empty result if the user did not enter a password"""
    return {
        'password': None,
        'strength': 0,
        'password_strengths': [],
        'password_weaknesses': [],
    }

def evaluate_password(request):
    """Evaluates the password and displays the results page"""

    # Redirects to the home page if the user searches for the results page in the search bar
    if request.method != 'POST':
        return redirect('PasswordCheck:index')

    password = request.POST.get('password')
    previous_password = request.POST.get('previous_password')
    personal_information = request.POST.get('personal_information')

    # Displays a "No password provided" message if no password was entered
    if not password:
        return render(request, 'PasswordCheck/check_password.html', empty_result())

    password_model = Password(password_text=password)
    password_model.save()
    password_model.calculate_password_attributes(previous_password, personal_information)
    password_model.calculate_password_strength()
    password_model.calculate_strengths_weaknesses()
    # Delete all passwords to ensure they are not saved in the system
    Password.objects.all().delete()

    # Display the results page
    return render(request, 'PasswordCheck/check_password.html', {
        'password': password,
        'strength': password_model.get_password_strength(),
        'password_strengths': password_model.get_password_strengths(),
        'password_weaknesses': password_model.get_password_weaknesses(),
    })