from django.shortcuts import render
from .models import Category, Community, Quiz
# from django.http import HttpResponse
import random
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
        selected_answers = request.POST.getlist('answer')
        correct_answers = 0
        total_questions = Quiz.objects.count()

        for i, answer in enumerate(selected_answers):
            question = Quiz.objects.all()[i]
            if question.answer == answer:
                correct_answers += 1

        score_percentage = (correct_answers / total_questions) * 100
        return render(request, 'quiz_result.html', {'score': score_percentage})
    questions = list(Quiz.objects.all()) 
    return render(request, 'quiz.html', {'questions_data': questions})

