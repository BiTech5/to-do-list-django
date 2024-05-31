from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from . import models
from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.method=='POST':
        todo_list=str(request.POST.get('todo_list'))
        if todo_list=="":
            print("error")
            return HttpResponse('Error')
        else:
            new_todo=models.Todo(user=request.user,task=todo_list)
            new_todo.save()
    data=models.Todo.objects.all()
    return render(request,'index.html',{'data':data})

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