from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Brands ,UserProfile,Bikes,cars,deal
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
import re
def Home_page(request):
    return render(request,"products/home.html")

def About_page(request):
    return render(request,"products/about.html")

def Contact_page(request):
    return render(request,"products/contact.html")

def Signup_page(request):
        if request.method == 'POST':
    
            name = request.POST.get('name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            termcond = request.POST.get('termcond')

            if not name or not name.isalpha():
                messages.success(request,'Name only character')
                return render(request, "products/signup.html")

            if not password or not len(password) > 7:
                messages.success(request,'Password must be at least 7 character')
                return render(request, "products/signup.html")

            try:
                validate_email(email)
            except ValidationError:
                messages.error(request, 'Invalid email address.')
                return render(request, "products/signup.html")

            phone_regex = re.compile(r'^\d{10}$')
            if not phone_regex.match(mobile):
                messages.error(request, 'Invalid phone number. Please enter a 10-digit number.')
                return render(request, "products/signup.html")
            else:
                user = User.objects.create_user(username=username, password=password,email=email)
                login(request, user)
    
                return render(request, "products/login.html")  
            

        return render(request, "products/signup.html")

def Login_page(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

        
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, "products/brands.html")
            else:
                
                messages.error(request,'Invalid username and password')
        return render(request,"products/login.html")

def contact_dealer(request):

    if request.method == 'POST':
        pin = request.POST.get('pin')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        en = deal(pin=pin,name=name,mobile=mobile)
        en.save()
        messages.success(request, 'Sent successfully.') 
    return render(request, "products/contactdealer.html")

def Addbikes(request):

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            Description1 = request.POST.get('Description1')  
            price = request.POST.get('price')
            engine = request.POST.get('engine')
            power = request.POST.get('power')
            torque = request.POST.get('torque')
            mileage = request.POST.get('mileage')
            weight = request.POST.get('weight')
            aboutcar = request.POST.get('aboutcar')
            logo = request.FILES.get('logo')
            img1 = request.FILES.get('img1')
            img2 = request.FILES.get('img2')
            img3 = request.FILES.get('img3')
            img4 = request.FILES.get('img4')
            img5 = request.FILES.get('img5')
            img6 = request.FILES.get('img6')
            img7 = request.FILES.get('img7')
            
        
            an = Bikes(name=name, Description1=Description1, price=price, engine=engine, power=power, torque=torque,
                       mileage=mileage, weight=weight, aboutcar=aboutcar, logo=logo, img1=img1, img2=img2, img3=img3,
                       img4=img4, img5=img5, img6=img6, img7=img7)
            
    
            an.save()
            
            
            messages.success(request, 'Bike added successfully.')
        except Exception as e:
        
            print("An error occurred:", e)
        
            messages.error(request, 'Failed to add bike. Please try again later.')
        
    return render(request, "products/bikeadd.html")

    
def Addcars(request):

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            Description1 = request.POST.get('Description1')  
            price = request.POST.get('price')
            engine = request.POST.get('engine')
            power = request.POST.get('power')
            torque = request.POST.get('torque')
            mileage = request.POST.get('mileage')
            weight = request.POST.get('weight')
            aboutcar = request.POST.get('aboutcar')
            logo = request.FILES.get('logo')
            img1 = request.FILES.get('img1')
            img2 = request.FILES.get('img2')
            img3 = request.FILES.get('img3')
            img4 = request.FILES.get('img4')
            img5 = request.FILES.get('img5')
            img6 = request.FILES.get('img6')
            img7 = request.FILES.get('img7')
            
    
            an = Brands(name=name, Description1=Description1, price=price, engine=engine, power=power, torque=torque,
                       mileage=mileage, weight=weight, aboutcar=aboutcar, logo=logo, img1=img1, img2=img2, img3=img3,
                       img4=img4, img5=img5, img6=img6, img7=img7)
            
    
            an.save()
            
    
            messages.success(request, 'Car added successfully.')
        except Exception as e:
    
            print("An error occurred:", e)
            
            messages.error(request, 'Failed to add bike. Please try again later.')
        
    return render(request, "products/caradd.html")


def Addscooty(request):

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            Description1 = request.POST.get('Description1')  
            price = request.POST.get('price')
            engine = request.POST.get('engine')
            power = request.POST.get('power')
            torque = request.POST.get('torque')
            mileage = request.POST.get('mileage')
            weight = request.POST.get('weight')
            aboutcar = request.POST.get('aboutcar')
            logo = request.FILES.get('logo')
            img1 = request.FILES.get('img1')
            img2 = request.FILES.get('img2')
            img3 = request.FILES.get('img3')
            img4 = request.FILES.get('img4')
            img5 = request.FILES.get('img5')
            img6 = request.FILES.get('img6')
            img7 = request.FILES.get('img7')
            
        
            an = cars(name=name, Description1=Description1, price=price, engine=engine, power=power, torque=torque,
                       mileage=mileage, weight=weight, aboutcar=aboutcar, logo=logo, img1=img1, img2=img2, img3=img3,
                       img4=img4, img5=img5, img6=img6, img7=img7)
            
            
            an.save()
            
        
            messages.success(request, 'Car added successfully.')
        except Exception as e:
            
            print("An error occurred:", e)
            
            messages.error(request, 'Failed to add bike. Please try again later.')
        
    return render(request, "products/scootyadd.html")


def brands_view(request):
    products = Brands.objects.all()
    context = {'products': products}
    return render(request, "products/home2.html", context)

def bike_view(request):
    products = Bikes.objects.all()
    context = {'products': products}
    return render(request, "products/bike.html", context)

def scooter_view(request):
    products = cars.objects.all()
    context = {'products': products}
    return render(request, "products/car.html", context)

def UserProfileView(request):
    return render(request, 'products/userprofile.html') 

def details(request,id):
    product = get_object_or_404(Brands,pk=id)
    context = {'product': product}
    return render(request,'products/cardetail.html',context)
def details1(request,id):
    product = get_object_or_404(Bikes,pk=id)
    context = {'product': product}
    return render(request,'products/bikedetail.html',context)
def details2(request,id):
    product = get_object_or_404(cars,pk=id)
    context = {'product': product}
    return render(request,'products/scootydetail.html',context)

def Logout(request):
    return render(request,'products/home.html')

def Home(request):
    return render(request,'products/brands.html')

def Back(request):
    return render(request,'products/brands.html')

def Back1(request):
    return render(request,'products/brands.html')

def Back2(request):
    return render(request,'products/bike.html')

def Back3(request):
    return render(request,'products/car.html')
def contactdeal(request):
    return render(request,'products/contactdealer.html')

def addbike(request):
    return render(request,'products/bikeadd.html')

def addcar(request):
    return render(request,'products/caradd.html')

def addscooty(request):
    return render(request,'products/scootyadd.html')

