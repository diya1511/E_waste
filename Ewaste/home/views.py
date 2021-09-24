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



# def handleSignUp(request):
#     if request.method=="POST":
#         # parameters
#         username=request.POST['username']
#         email=request.POST['email']
#         firstname=request.POST['firstname']
#         lname=request.POST['lname']
#         pass1=request.POST['pass1']
#         pass2=request.POST['pass2']

#         # check for errorneous input
#         if len(username)<10:
#             messages.error(request, " Your user name must be under 10 characters")
#             return redirect('/')

#         if not username.isalnum():
#             messages.error(request, " User name should only contain letters and numbers")
#             return redirect('/')
#         if (pass1!= pass2):
#              messages.error(request, " Passwords do not match")
#              return redirect('/')
#         # Create the user
#         myuser = User.objects.create_user(username, email, pass1)
#         myuser.first_name= firstname
#         myuser.last_name= lname
#         myuser.save()
#         messages.success(request, "hi"+firstname+"your account has beet successfully created")
#         return redirect('/')

#     else:
#         return HttpResponse("404 - Not found")

# def handeLogin(request):
#     if request.method=="POST":
#         # Get the post parameters
#         loginuser=request.POST['loginuser']
#         loginpassword=request.POST['loginpassword']

#         user=authenticate(username= loginuser, password= loginpassword)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Successfully Logged In")
#             return redirect("/")
#         else:
#             messages.error(request, "Invalid credentials! Please try again")
#             return redirect("/")

#     return HttpResponse("404- Not found")
   

#     return HttpResponse("login")

# def handelLogout(request):
#     logout(request)
#     messages.success(request, "Successfully logged out")
#     return redirect('home')
 