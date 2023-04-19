from django.urls import path
from . import views
urlpatterns =[
path('', views.home, name='myApp-home'),
path('about/', views.about, name='myApp-about'),
path('contact/', views.contact, name='myApp-contact'),
path('rg/', views.rg, name='myApp-rg'),
]
