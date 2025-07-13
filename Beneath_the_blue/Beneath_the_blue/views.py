from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Question, Option, QuizResult
import random

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quiz')
    else:
        form = UserCreationForm()
    return render(request, 'quiz/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('quiz')
    else:
        form = AuthenticationForm()
    return render(request, 'quiz/login.html', {'form': form})

@login_required
def quiz(request):
    if request.method == 'POST':
        score = 0
        total = 0
        for key, value in request.POST.items():
            if key.startswith('question_'):
                qid = int(key.split('_')[1])
                selected = int(value)
                question = Question.objects.get(id=qid)
                correct = question.options.filter(is_correct=True).first()
                if correct and correct.id == selected:
                    score += 1
                total += 1
        QuizResult.objects.create(user=request.user, score=score, total_questions=total)
        return render(request, 'quiz/result.html', {'score': score, 'total': total})
    questions = list(Question.objects.all())
    selected_questions = random.sample(questions, min(len(questions), 5))
    return render(request, 'quiz/quiz.html', {'questions': selected_questions})

@login_required
def summary(request):
    results = QuizResult.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'quiz/summary.html', {'results': results})

def threats_solution(request):
    return render(request, 'threats_solution.html')