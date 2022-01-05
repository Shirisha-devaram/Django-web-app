from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse 
from django.contrib import messages
import requests
from requests.structures import CaseInsensitiveDict
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pass1']
        
        user = authenticate(email=email, password=pass1)
        # print(user)
        
        if user is not None:
            login(request, user)
            return redirect('/details/')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('/')
    
    return render(request,'main.html')

def signup(request):
    if(request.method=="POST"):
        print("came here")
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        address=request.POST['address']
        print(username)
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        # if len(username)>20:
        #     messages.error(request, "Username must be under 20 charcters!!")
        #     return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.address= address
        myuser.save()
        messages.success(request, "your Account has been created succesfully!! Please login again with your credentials.")
        return redirect('/')

    return render(request,'signup.html')


def editcus_view(request):
    return render(request, "editUser.html")
def userlist(request):
    user=User.objects.all()
    print(user)
    return render(request, "user/user_details.html",{'user':user})
class UpdateUser(UpdateView):
    model=User
    fields=['username','email','password','address']
    success_url = '/details/'
class DeleteUser(DeleteView):
    model=User
    success_url = '/details/'
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('/')