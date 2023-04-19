from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'myApp/home.html')
def about(request):
    return render(request, 'myApp/about.html')
def contact(request):
    return render(request, 'myApp/contact.html')



# Create your views here.
