from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .models import *
# Create your views here.



def index(request):
    
    groceries  = Groceries.objects.all()
    household = HouseHold.objects.all()

    context = {
        'groceries' : groceries,
        'household' : household,
    }

    return render(request, 'index.html', context)

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            messages.add_message(request,messages.SUCCESS,"Oturum acma basarili")
            return redirect('index')
        else:  
            messages.add_message(request, messages.ERROR,"Oturum acma basarisiz")
            return redirect('login')

    else:
        return render(request,"login.html")


def logout(request):
    if request.method=="POST":
        auth.logout(request)
        messages.add_message(request,messages.SUCCESS,"Cikis islemi basarili")
        return redirect('index')


def cart(request, cart_id):
    products = Cart_Products.objects.filter(cart_id = cart_id)
    number = Cart_Products.objects.filter(cart_id = cart_id).count()
    context = {
        'cart' : products,
        'number' : number
    }

    return render(request, 'cart.html', context)

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        #get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['password2']
        first_name = request.POST['first_name']

        if password == repassword:
            # Username control
            if User.objects.filter(username= username).exists():
                messages.add_message(request,messages.WARNING,"Bu kullanici ad daha once alinmistir")
                return redirect('register')
            
            else:
                if User.objects.filter(email= email).exists():
                    messages.add_message(request,messages.WARNING,"Bu email daha once alinmistir")
                    return redirect('register')

                else:
                    # her sey guzel 
                    # kayit islemi yapilabilir
                    user=User.objects.create_user(username=username, email=email, password=password, first_name = first_name)
                    user.save()
                    messages.add_message(request,messages.SUCCESS,"Kullanici olusturma islemi basarili")
                    return redirect('login')
        else:
            messages.add_message(request,messages.WARNING,"Parolalar eslesmiyor")
            return redirect('register')
    else:
        return render(request,"register.html")


def products(request):
    return render(request, 'products.html')

def beverages(request, pr_id):
    beverages = Beverages.objects.all()

    if pr_id != 0:
        cart = Cart.objects.get(id = 1)
        beverage = Beverages.objects.get(id = pr_id)
        carts = Cart_Products.objects.create(cart_id=cart, beverages_id=beverage)
        carts.save()

    context = {
        'beverages' : beverages
    }
    return render(request, 'beverages.html', context)

def faq(request):
    return render(request, 'faq.html')

def groceries(request, pr_id):
    groceries = Groceries.objects.all()
    if pr_id != 0:
        cart = Cart.objects.get(id = 1)
        grocery = Groceries.objects.get(id = pr_id)
        carts = Cart_Products.objects.create(cart_id=cart, groceries_id=grocery)
        carts.save()
    context = {
        'groceries' : groceries
    }

    return render(request, 'groceries.html', context)

def household(request, pr_id):
    household = HouseHold.objects.all()
    if pr_id != 0:
        cart = Cart.objects.get(id = 1)
        households = HouseHold.objects.get(id = pr_id)
        carts = Cart_Products.objects.create(cart_id=cart, household_id=households)
        carts.save()
    
    context = {
        'household' : household
    }

    return render(request, 'household.html', context)

def personalcare(request, pr_id):
    personalcare = Personal_Care.objects.all()
    if pr_id != 0:
        cart = Cart.objects.get(id = 1)
        personalcares = Personal_Care.objects.get(id = pr_id)
        carts = Cart_Products.objects.create(cart_id=cart, personal_care_id=personalcares)
        carts.save()
    
    
    context = {
        'personalcare' : personalcare
    }

    return render(request, 'personalcare.html', context)

def about(request):
    return render(request, 'about.html')


def packagedfoods(request, pr_id):
    packagedfoods = Packaged_Foods.objects.all()
    if pr_id != 0:
        cart = Cart.objects.get(id = 1)
        packagedfood = Packaged_Foods.objects.get(id = pr_id)
        carts = Cart_Products.objects.create(cart_id=cart, packaged_foods_id=packagedfood)
        carts.save()
    
    context = {
        'packagedfoods' : packagedfoods
    }
    return render(request, 'packagedfoods.html', context)

    