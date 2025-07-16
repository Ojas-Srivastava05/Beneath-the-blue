from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .forms import PledgeForm, IdeaForm, FeedbackForm, NewsletterForm
from .models import Pledge, Idea, Feedback, Subscriber

def home(request):
    return render(request, 'ocean/index.html')

@require_http_methods(["POST"])
def submit_pledge(request):
    if request.method == 'POST':
        form = PledgeForm(request.POST)
        if form.is_valid():
            pledge = form.save()
            return JsonResponse({'success': True, 'message': 'Thank you for your pledge!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

@require_http_methods(["POST"])
def submit_idea(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save()
            return JsonResponse({'success': True, 'message': 'Thank you for sharing your idea!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

@require_http_methods(["POST"])
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            return JsonResponse({'success': True, 'message': 'Thank you for your feedback!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

@require_http_methods(["POST"])
def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subscriber, created = Subscriber.objects.get_or_create(
                email=email,
                defaults={'is_active': True}
            )
            if not created:
                subscriber.is_active = True
                subscriber.save()
            return JsonResponse({'success': True, 'message': 'Thank you for subscribing!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)