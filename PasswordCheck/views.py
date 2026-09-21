from django.shortcuts import render
from django.http import HttpResponse
from .models import Password

# Create your views here.
def index(request):
    return render(request, 'PasswordCheck/index.html')

def evaluate_password(request):
    password = request.POST.get('password')
    strength = request.POST.get('strength')
    return render(request, 'PasswordCheck/check_password.html', {'password': password, 'strength': strength})