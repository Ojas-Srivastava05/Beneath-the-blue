from django.shortcuts import render
from django.urls import reverse
from .models import EndangeredSpecies

# Create your views here.
def endangered_species(request):
    animals = EndangeredSpecies.objects.all()
    navbar_links = [
        # {"url": reverse('species_home'), "text": "Species Home"},
        {"url": reverse('endangered_species'), "text": "Endangered"},
        {"url": reverse('explore_map'), "text": "Explore"},
    ]
    return render(request, 'Endangered_species.html', {'animals': animals, 'navbar_links': navbar_links})

def ocean(request):
    # navbar_links = [
    #     {"url": reverse('species_home'), "text": "Species Home"},
    #     {"url": reverse('endangered_species'), "text": "Endangered"},
    #     {"url": reverse('explore_map'), "text": "Explore"},
    # ]
    animals = EndangeredSpecies.objects.all()
    return render(request, 'Endangered_species.html', {"animals": animals})