from django.shortcuts import render
from users import forms

def index(request):

    return render(request, 'inicio/index.html')