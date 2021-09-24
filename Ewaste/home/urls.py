from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("",views.home, name='home') ,
    path("home/",views.home, name='home') ,
    path("about/",views.about, name='about') ,
    path("contact/",views.contact, name='contact') ,
    path("services/",views.services, name='services') ,
    path('lin/' , views.lin , name = 'login'),
    path('lout/', views.lout, name="logout"),
    path('register/' , views.register , name = 'register'),
    path('about/lin' , views.lin , name = 'al'),
    path('about/register' , views.register , name = 'ar'),
    path('home/lin' , views.lin , name = 'al'),
    path('home/register' , views.register , name = 'ar'),
    path('contact/lin' , views.lin , name = 'cl'),
    path('contact/register' , views.register , name = 'cr'),
    path('services/lin' , views.lin , name = 'sl'),
    path('services/register' , views.register , name = 'sr'),
]