from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .forms import PledgeForm, IdeaForm, FeedbackForm, NewsletterForm
from .models import Pledge, Idea, Feedback, Subscriber
from django.urls import reverse

def home(request):
    navbar_links = [
        {"url": reverse('home'), "text": "Home"},
        {"url": reverse('explore_map'), "text": "Explore"},
        {"url": reverse('threats'), "text": "Threats"},
        {"url": reverse('endangered_species'), "text": "Species"},
        {"url": reverse('community_page'), "text": "Community"},
    ]
    quick_facts = [
        {"number": "71%", "text": "of Earth's surface is ocean"},
        {"number": "80%", "text": "of ocean life is undiscovered"},
        {"number": "50-80%", "text": "of our oxygen comes from the sea"},
        {"number": "10%", "text": "of oceans have been explored"},
    ]
    features = [
        {
            "id": "explore",
            "title": "Deep Sea Explorer",
            "desc": "Navigate through marine ecosystems from sunlit surfaces to the mysterious midnight zone.",
            "btn_text": "Begin Exploration",
            "btn_url": reverse('explore_map'),
            "img": "images/deep.avif",
            "img_alt": "Deep ocean with submarine lights"
        },
        {
            "id": "threats",
            "title": "Threats Below Surface",
            "desc": "See how pollution is destroying marine ecosystems worldwide.",
            "btn_text": "View Threats",
            "btn_url": reverse('threats'),
            "img": "images/threats.jpg",
            "img_alt": "Plastic waste covering ocean surface"
        },
        {
            "id": "solutions",
            "title": "Hope From the Deep",
            "desc": "Discover innovative solutions restoring our oceans.",
            "btn_text": "Learn Solutions",
            "btn_url": "#solutions",
            "img": "image/solutions.jpg",
            "img_alt": "Team cleaning ocean pollution"
        },
    ]
    return render(request, 'ocean/index.html', {"navbar_links": navbar_links, "quick_facts": quick_facts, "features": features})

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