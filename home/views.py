from django.shortcuts import render,HttpResponse,redirect
from home.models import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'index.html')


def explore_map(request):
    return  render(request, 'explore.html')

def endangered_species(request):
    return render(request, 'Endangered_species.html')

def threats(request):
    return render(request, 'threats-solution.html')

def submit_pledge(request):
    if request.method == 'POST':
        # Handle pledge submission
        return JsonResponse({'success': True, 'message': 'Pledge submitted successfully!'})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def submit_idea(request):
    if request.method == 'POST':
        # Handle idea submission
        return JsonResponse({'success': True, 'message': 'Idea submitted successfully!'})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def submit_feedback(request):
    if request.method == 'POST':
        # Handle feedback submission
        return JsonResponse({'success': True, 'message': 'Feedback submitted successfully!'})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def subscribe(request):
    if request.method == 'POST':
        # Handle newsletter subscription
        return JsonResponse({'success': True, 'message': 'Successfully subscribed!'})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})
 
# sing in function
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

# logout function not working adding in home page after work on it
# def logout(request):
#     # user = loging.objects.first()  # Gets the first user or None
#     # user.delete()
#     return  HttpResponse("You have been logged out successfully.")

# sing up function
def sign_up(request):
    if request.method=="POST":
        user_id=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        if password != password2:
            return render(request, 'sign_up.html', {'error': 'Passwords do not match. Please try again.'})
        user = authenticate(request, username=user_id, password=password)
        
        # Check if the user already exists
        if loging.objects.filter(user_id=user_id).exists():
            return render(request, 'sign_up.html', {'error': 'User already exists. Please sign in.'})
       
        # Create a new use
        register= loging(user_id= user_id,password=password) 
        register.save()
    return render(request,"sign_up.html")

