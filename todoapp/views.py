from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        usernmae=request.POST.get('username')
        password=request.POST.get('password')
        valid=auth.authenticate(username=usernmae,password=password)
        if valid is not None:
            auth.login(request,valid)
            return redirect('home')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first=request.POST.get('fir_name')
        last=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        passw1=request.POST.get('password1')
        passw2=request.POST.get('password2')
        new_user=User.objects.create_user(first_name=first,last_name=last,username=username,email=email,password=passw1)
        new_user.save()
        return redirect('login')
        # print(first,last)
    return render(request,'register.html')