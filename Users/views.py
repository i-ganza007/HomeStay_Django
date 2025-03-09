from django.shortcuts import render
from .serializers import Event

def home(request):
    return render('home.html')