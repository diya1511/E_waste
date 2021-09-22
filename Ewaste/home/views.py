from django.shortcuts import render,redirect
from django.http.response import HttpResponseNotAllowed
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import auth , User 
from django.contrib.auth  import authenticate,  login, logout
def home(request):
    return render(request,"home.html")
 
def about(request) :
    return render(request,"about.html")
def contact(request) :
    if request.method == 'POST' :
      name = request.POST.get('name')
      email= request.POST.get('email')
      phone = request.POST.get('phone')
      desc = request.POST.get('desc')
      address = request.POST.get('address')
      contact =Contact(name=name,email=email,phone=phone,desc=desc,address=address,date= datetime.today())
      contact.save()
      messages.success(request, 'Your message has been sent!')
    return render(request,"contact.html")

def services(request) :
    return render(request,"services.html")