from django.shortcuts import render,redirect
from .models import  *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
# Create your views here.


# This view renders the community page where users can learn about the Beneath The Blue community and its mission.
def community_page(request):
    Category_data = Category.objects.all()
    # Try to get category id from GET, else use first category's id
    id = request.GET.get('category') or (Category_data.first().id if Category_data.exists() else None)
    try:
        Category_selected = Category.objects.get(id=id)
        Community_data = Community.objects.filter(category=Category_selected)
    except (Category.DoesNotExist, TypeError, ValueError):
        Category_selected = None
        Community_data = Community.objects.none()

    data = {
        'Community_data': Community_data,
        'Category_data': Category_data,
        'Category_selected': Category_selected
    }
    return render(request, 'community.html', data)


# @login_required
def quiz(request):
    if request.method == 'POST':
        questions = Quiz.objects.all()
        score = 0
        total = questions.count()

        for question in questions:
            submitted_answer = request.POST.get(f'question_{question.id}')
            if submitted_answer:
                try:
                    if int(submitted_answer) == question.answer:
                        score += 1
                except (ValueError, TypeError):
                    # Handle cases where submitted_answer is not a valid integer
                    pass
        
        context = {
            'score': score,
            'total': total,
            'correct': score,
            'wrong': total - score,
        }
        return render(request, 'result.html', context)

    questions = list(Quiz.objects.all()) 
    return render(request, 'quiz.html', {'questions_data': questions})

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