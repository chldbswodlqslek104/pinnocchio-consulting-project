from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def index(request):
    return render(request, 'html/first-screen.html')

#HttpResponse("Hello, world. You're at the polls index.")

#render(request, 'C:/last/hosting/src/html/first-screen.html')
