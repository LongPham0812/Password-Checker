from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Password Checker - Enter a password here.")

def evaluate_password(request, password, strength):
    return HttpResponse("Password \"%s\" has strength score of %s" % (password, strength))