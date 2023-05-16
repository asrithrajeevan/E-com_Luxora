from django.shortcuts import render
from .models import Items, User

# Create your views here.

def index(request):
    item_dict = {
        'items' : Items.objects.all
    }
    return render(request, 'index.html', item_dict)

def signup(request):
    if request.method == "POST":
        sign = User(
            user_firstname = request.POST.get('firstname'),
            user_lastname = request.POST.get('lastname'),
            user_name = request.POST.get('username'),
            user_dob = request.POST.get('dob'),
            user_gender = request.POST.get('gender'),
            user_phone = request.POST.get('phonenumber'),
            alt_phone = request.POST.get('altnumber'),
            user_pin = request.POST.get('pin'),
            user_place = request.POST.get('place'),
            user_country = request.POST.get('country'),
            user_email = request.POST.get('email'),
            user_address = request.POST.get('address'),
            )
        sign.save()
   
    return render(request, "signup.html")

def loging(request):
    print('yes out')
    if request.method == "POST":
        user = request.POST.get('fname')
        user_pass = request.POST.get('password')


    return render(request, 'loging.html')

