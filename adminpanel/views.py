from django.shortcuts import render, redirect, get_object_or_404
from .models import Category,Product
from .forms import CategoryForm, ProductForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/sign_in/')
def home(request):
     products = Product.objects.all().order_by('-id')
     return render(request,'adminpanel/home.html',{'products':products})

@login_required(login_url='/sign_in/')
def category_list(request):
    categories = Category.objects.all().order_by('-id')
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'A new category is added')
            return redirect('adminpanel:category_list')
    else:
        form = CategoryForm()
    context = {
        'form':form,
        'categories':categories
    }
    return render(request,'adminpanel/category_list.html',context)

@login_required(login_url='/sign_in/')
def edit_category(request,category_id):
    category = get_object_or_404(Category, id = category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance = category)
        if form.is_valid():
            form.save()
            messages.success(request,'Category is updated')
            return redirect('adminpanel:category_list')
    else:
        form = CategoryForm(instance = category)

    context ={
        'form':form
        
        }
    return render(request,'adminpanel/edit_category.html', context)

@login_required(login_url='/sign_in/')
def delete_category(request, category_id):
    category = get_object_or_404(Category, id = category_id)   
    category.delete()
    messages.success(request,'Category Deleted Successfully')
    return redirect('adminpanel:category_list')

@login_required(login_url='/sign_in/')  
def add_product(request, category_id):
    category = get_object_or_404(Category, id= category_id)
    request.session['category_id'] = category_id
    products = Product.objects.filter(category = category).order_by('-id')
    if request.method =='POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.category = category
            product.save()
            messages.success(request,'A new product is added')
            return redirect('adminpanel:add_product', category_id  = category_id)

    else:
        form = ProductForm()

    context ={
        'form':form,
        'products':products
    }
    return render(request,'adminpanel/add_product.html',context)

@login_required(login_url='/sign_in/')
def edit_product(request, product_id):
    category_id = request.session.get('category_id',0)    
    product = get_object_or_404(Product, id = product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance = product)
        if form.is_valid():
            form.save()
            messages.success(request,'Product is updated')
            return redirect('adminpanel:add_product', category_id  = category_id)
    else:
        form = ProductForm(instance = product)

    context ={
        'form':form
        
        }

    return render(request,'adminpanel/edit_products.html',context)

@login_required(login_url='/sign_in/')
def delete_product(request,product_id):
    category_id = request.session.get('category_id',0)
    product = get_object_or_404(Product, id = product_id)   
    product.delete()
    messages.success(request,'Product Deleted Successfully')
    return redirect('adminpanel:add_product', category_id  = category_id)

@login_required(login_url='/sign_in/')
def sign_out(request):
    logout(request)
    return redirect('sitevisitor:home')