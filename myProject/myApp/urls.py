from django.urls import path
from . import views
urlpatterns =[
path('', views.home, name='myApp-home'),
path('about/', views.about, name='myApp-about'),
path('contact/', views.contact, name='myApp-contact'),
path('reg/', views.reg, name='myApp-reg'),
path('profile/', views.profile, name='myApp-profile'),
path('login/', views.login, name='myApp-login'),
path('review/', views.review, name='myApp-review'),
path('password/', views.password, name='myApp-password'),
]
