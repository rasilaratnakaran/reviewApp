from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1> Welcome to Electro World- Home</h1>')
def about(request):
    return HttpResponse('<h1> Welcome to Electro World- About Us</h1>')
def contact(request):
    return HttpResponse('<h1> Welcome to Electro World- Contact Us</h1>')

# Create your views here.
