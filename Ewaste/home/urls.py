from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home, name='home') ,
    path("home/",views.home, name='home') ,
    path("about/",views.about, name='about') ,
    path("contact/",views.contact, name='contact') ,
    path("services/",views.services, name='services') ,
    path('login/' , views.login , name = 'login'),
   
]