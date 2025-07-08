from django.shortcuts import render, redirect
from newapp.models import Order ,Contact
from django.http import HttpResponse

from django.contrib import messages  # Import the messages framework
# Create your views here.
def home(request):
    return render(request, 'home.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        print(f"Name: {name}, Email: {email}, Message: {message}")  # Check if data is received correctly

        if name and email and message:  # Optional check if data is present
            contact = Contact(name=name, email=email, message=message)
            contact.save()
            
            # Add a success message
            messages.success(request, 'Your message has been forwarded successfully! 🎉')

            return redirect('home')  # Redirect after saving data
        else:
            return render(request, 'contact.html', {'error': 'Please fill in all fields.'})

    return render(request, 'contact.html')


   


def about(request):
    return render(request, 'about.html')
def signup(request):
    return render(request, 'signup.html')
def Commercial(request):
    return render(request, 'Commercial.html')    
def Domestic(request):
    return render(request, 'Domestic.html') 
def login(request):
    return render(request, 'login.html')     
def buffalows(request):
    return render(request, 'buffalows.html')     
def cows(request):
    return render(request, 'cows.html') 
from django.shortcuts import render, redirect
from .models import Order

def order_form(request):
    if request.method == "POST":
        method = request.POST.get("method")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        quantity = request.POST.get("quantity")
        delivery_time = request.POST.get("delivery_time")

        # Save to database
        Order.objects.create(
            method=method,
            phone=phone,
            address=address,
            quantity=quantity,
            delivery_time=delivery_time
        )
        return redirect('order_success')  

    return render(request, "order_form.html")  

def order_success_view(request):
    return render(request, "order_success.html")

  
