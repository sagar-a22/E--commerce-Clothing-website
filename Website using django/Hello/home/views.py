from django.shortcuts import render, HttpResponse,redirect
# from home.models import Contact
from home.models import Contact
from home.models import Product
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login


# Create your views here.

def index(request):
    
    if  request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')
    # return HttpResponse("This is my homepage")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
     if request.method == "POST":
         name=request.POST.get('name')
         address=request.POST.get('address')
         email=request.POST.get('email')
         phone=request.POST.get('phone')
         contact= Contact(name=name , address=address,email=email,phone=phone)
         contact.save()
         messages.success(request, "Form has been submitted")
     return render(request, 'contact.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def loginuser(request):
    if request.method== "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        print(username,password)

        user= authenticate(username=username, password=password)


        if user is not None:
            login(request,user)
            return redirect('/')
        
        else:
            return render(request,'login.html')     

    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')

def signinuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Create a new user
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "User registered successfully. Please log in.")
            return redirect('/login')
        except Exception as e:
            messages.error(request, "Error ")
            return render(request, 'signin.html')

    return render(request, 'signin.html')

def detail(request, product_id):
    product = Product.objects.get(id=product_id)  # Fetch the specific product by ID
    return render(request, 'product_detail.html', {'product': product})

def buy(request):
    return render(request,'buynow.html')
