from django.shortcuts import render,redirect
from adminpanel.models import Product
from .forms import Registration_Form, Login_Form
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    products = Product.objects.all().order_by('-id')     
    return render(request,'sitevisitor/home.html',{'products':products})

def register_user(request):
    if request.method == 'POST':
        form = Registration_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Registered successfully!!!')
            return redirect('sitevisitor:home')
    else:
        form = Registration_Form()
    context={
        'form':form
    }
    return render(request, 'sitevisitor/register.html',context)

def user_login(request):
    
    if request.method =='POST':
        form = Login_Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('adminpanel:home')
                else:
                    return redirect('sitevisitor:user_home')
    else:
        form = Login_Form()
    context ={
        'form':form
    }
    return render(request,'sitevisitor/login.html',context)

def user_home(request):
    logged_user = request.user
    context={
        'user':logged_user
    }
    return render(request,'sitevisitor/user_home.html',context)