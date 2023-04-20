from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'myApp/home.html')
def about(request):
    return render(request, 'myApp/about.html')
def contact(request):
    return render(request, 'myApp/contact.html')
<<<<<<< HEAD



=======
def reg(request):
    return render(request, 'myApp/reg.html')
def profile(request):
    return render(request, 'myApp/profile.html')
def login(request):
    return render(request, 'myApp/login.html')
def review(request):
    return render(request, 'myApp/review.html')
def password(request):
    return render(request, 'myApp/password.html')
>>>>>>> b30e92c (about added)
# Create your views here.
