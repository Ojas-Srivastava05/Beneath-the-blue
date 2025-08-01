from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .forms import PledgeForm, IdeaForm, FeedbackForm
# from .models import Subscriber

def home(request):
    # if request.method == 'POST':
    #     pledge_form = PledgeForm(request.POST)
    #     idea_form = IdeaForm(request.POST)
    #     feedback_form = FeedbackForm(request.POST)
        
    #     if pledge_form.is_valid():
    #         pledge_form.save()
    #     if idea_form.is_valid():
    #         idea_form.save()
    #     if feedback_form.is_valid():
    #         feedback_form.save()
        
    #     return JsonResponse({'status': 'success'})
    return render(request, 'ocean/index.html')

def submit_pledge(request):
    if request.method == 'POST':
        form = PledgeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
    else:
        form = PledgeForm()
    return render(request, 'ocean/index.html', {'form': form})


def submit_idea(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
    else:
        form = IdeaForm()
    return render(request, 'ocean/index.html', {'form': form})

def submit_feedback(request):   
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
    else:
        form = FeedbackForm()
    return render(request, 'ocean/index.html', {'form': form})