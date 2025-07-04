from django.shortcuts import render,HttpResponse,redirect
from home.models import *
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
>>>>>>> Community
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def explore_map(request):
    return  render(request, 'explore.html')

<<<<<<< HEAD
=======
# sing in function
>>>>>>> Community
def sign_in(request):
    if request.method=="POST":
        user_id=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request, username=user_id, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('explore_map')
        else:
            return render(request, 'sign_in.html', {'error': 'Invalid credentials. Please try again.'})
    return render(request,"sign_in.html")
<<<<<<< HEAD
=======

# logout function not working adding in home page after work on it
>>>>>>> Community
def logout(request):
    # user = loging.objects.first()  # Gets the first user or None
    # user.delete()
    return  HttpResponse("You have been logged out successfully.")
<<<<<<< HEAD
=======

# sing up function
>>>>>>> Community
def sign_up(request):
    if request.method=="POST":
        user_id=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        if password != password2:
            return render(request, 'sign_up.html', {'error': 'Passwords do not match. Please try again.'})
        user = authenticate(request, username=user_id, password=password)
        
        # Check if the user already exists
<<<<<<< HEAD
        if User.objects.filter(username=user_id).exists():
            return render(request, 'sign_up.html', {'error': 'User already exists. Please log in.'})
=======
        if loging.objects.filter(user_id=user_id).exists():
            return render(request, 'sign_up.html', {'error': 'User already exists. Please sign in.'})
>>>>>>> Community
       
        # Create a new use
        register= loging(user_id= user_id,password=password) 
        register.save()
    return render(request,"sign_up.html")