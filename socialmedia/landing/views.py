from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


class Index(View):
    def get(self,request,*args,**kwargs):
        return render(request,'landing/index.html')
    
def login_page(request):
    if request.method=="POST":
        user_name=request.POST.get('Username')
        pas=request.POST.get('password')
        
        user=User.objects.filter(username=user_name)
        if(not user.exists()):
            messages.error(request,'Invalid User Name')
            return redirect('/login')
        
        user=authenticate(username=user_name,password=pas)
        
        if user is None:
            messages.error(request,"Invalid password")
            return redirect("/login")
        else:
            login(request,user)
            return redirect('/room')
    return render(request,'landing/login.html')
        
def reg_page(request):
    if request.method=='POST':
        name=request.POST.get('firstname')
        user_name=request.POST.get('Username')
        mail=request.POST.get('email')
        pas=request.POST.get('password')
        
        user=User.objects.filter(username=user_name)
        if(user.exists()):
            messages.error(request,"Username Already Exists")
            return redirect('/register')
        user=User.objects.create(first_name=name,username=user_name,email=mail,password=pas)
        user.set_password(pas)
        user.save()
        
        messages.info(request,"Account created successfully.")
        return redirect('/register')
    return render(request,'landing/register.html')

def log_out_page(request):
    logout(request)
    return redirect('/login')