from django.shortcuts import render, redirect
from .models import Password

# Create your views here.
def index(request):
    Password.objects.all().delete()
    return render(request, 'PasswordCheck/index.html')

def empty_result():
    return {
        'password': None,
        'strength': 0,
        'password_strengths': [],
        'password_weaknesses': [],
    }

def evaluate_password(request):
    if request.method != 'POST':
        return redirect('PasswordCheck:index')

    password = request.POST.get('password')
    previous_password = request.POST.get('previous_password')
    personal_information = request.POST.get('personal_information')

    if not password:
        return render(request, 'PasswordCheck/check_password.html', empty_result())

    password_model = Password(password_text=password)
    password_model.save()
    password_model.calculate_password_attributes(previous_password, personal_information)
    password_model.calculate_password_strength()
    password_model.calculate_strengths_weaknesses()
    Password.objects.all().delete()

    return render(request, 'PasswordCheck/check_password.html', {
        'password': password,
        'strength': password_model.get_password_strength(),
        'password_strengths': password_model.get_password_strengths(),
        'password_weaknesses': password_model.get_password_weaknesses(),
    })