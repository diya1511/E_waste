from django.shortcuts import render,redirect
from django.http.response import HttpResponseNotAllowed
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import auth , User 
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.decorators import login_required
import logging
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



def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['password2']
            coun = request.POST['coun']
            gen = request.POST['gen']
            a = request.POST['a']
            
            
            if len(username)>10 and len(username)<5:
                messages.error(request,"Username must be under 10 characters and more than 5characters")
                return redirect('register')

            if password == password2 :
                if User.objects.filter(email=email).exists():
                    messages.info(request , 'Email already used')
                    return redirect('register')
                elif User.objects.filter(username=username).exists():
                    messages.info(request , 'Username Already Used' )
                    return redirect('register')
                else:
                    user = User.objects.create_user(email=email , username=username ,password=password)
                    user.name = name 
                    user.save();
                    messages.success(request,"Your account has been succesfully created !!!")
                    return redirect('/lin')
            else:
                messages.info(request , 'Password is not same, try again !!!')
                return redirect('register')
        else:
                return render(request , 'register.html')

def lin(request):
    
        if request.method == 'POST':
                loginusername = request.POST ['loginusername']
                loginpassword = request.POST['loginpassword']

                user = authenticate(request,username=loginusername , password=loginpassword)
                print(user)
                if user is not None:
                        login(request , user)
                        messages.success(request,"Successfully logged in")
                        return redirect('home')
                else:
                    messages.error(request , 'invalid credentials, please try again')
                    return redirect('login')
        else: 
            return render ( request , 'login.html')

@login_required
def lout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')
