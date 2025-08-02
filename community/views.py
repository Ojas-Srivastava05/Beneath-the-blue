from django.shortcuts import render,redirect
from .models import  *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
import random
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, PostMedia, Comment
from .forms import PostForm, PostEditForm, CommentForm
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


# from django.shortcuts import render
# from .models import Question
# import random

def quiz(request):
    # Get all questions and shuffle them
    all_questions = list(Question.objects.all())
    random.shuffle(all_questions)
    
    # Store shuffled questions in session
    request.session['shuffled_questions'] = [q.id for q in all_questions]
    request.session['current_question_index'] = 0
    request.session['score'] = 0
    
    return render(request, 'quiz.html', {
        'question': all_questions[0]
    })

def next_question(request):
    if request.method == 'POST':
        # Process answer if submitted
        # You'll need to add this logic
        
        # Get next question
        current_index = request.session.get('current_question_index', 0)
        question_ids = request.session.get('shuffled_questions', [])
        
        if current_index + 1 < len(question_ids):
            next_question = Question.objects.get(id=question_ids[current_index + 1])
            request.session['current_question_index'] = current_index + 1
            return render(request, 'quiz.html', {
                'question': next_question
            })
        else:
            # Quiz completed
            score = request.session.get('score', 0)
            return render(request, 'result.html', {
                'score': score,
                'total': len(question_ids)
            })
    
    return redirect('quiz')

# Create your views here.
def home(request):
    return render(request, 'index.html')


def explore_map(request):
    return  render(request, 'explore.html')


def threats(request):
    threats = Threat.objects.all()
    return render(request, 'threats-solution.html', {'threats': threats})


 
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

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def community_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'community_posts.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
            files = request.FILES.getlist('media')
            for file in files:
                PostMedia.objects.create(post=post, file=file)
                
            return redirect('community_posts')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'my_posts.html', {'posts': posts})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    
    if request.method == 'POST':
        form = PostEditForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            
            files = request.FILES.getlist('new_media')
            for file in files:
                PostMedia.objects.create(post=post, file=file)
                
            return redirect('my_posts')
    else:
        form = PostEditForm(instance=post)
    
    return render(request, 'edit_post.html', {
        'form': form,
        'post': post
    })

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'total_likes': post.likes.count()})

@login_required
def delete_media(request, media_id):
    media = get_object_or_404(PostMedia, id=media_id, post__author=request.user)
    if request.method == 'POST':
        media.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('community_posts')
    return redirect('community_posts')