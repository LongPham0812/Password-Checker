from django.shortcuts import render
from django.http import HttpResponse
from .models import Password

# Create your views here.
def index(request):
    return render(request, 'PasswordCheck/index.html')

def evaluate_password(request):
    password = request.POST.get('password')
    previous_password = request.POST.get('previous_password')
    common_words = request.POST.get('common_words')
    personal_information = request.POST.get('personal_information')
    password_model = Password(password_text=password)
    password_model.save()

    if password:
        password_model.calculate_password_attributes(previous_password, common_words, personal_information)
        password_model.calculate_password_strength()

    return render(request, 'PasswordCheck/check_password.html', {'password': password, 'strength': password_model.get_password_strength()})