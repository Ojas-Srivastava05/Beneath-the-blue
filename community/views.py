from django.shortcuts import render
from .models import Community, Category
# Create your views here.


# This view renders the community page where users can learn about the Beneath The Blue community and its mission.
def community_page(request):
    Community_data = Community.objects.all()
    Category_data = Category.objects.all()
    id =  Category_data.first().id  # default to the first category if no query parameter is provided
    if request.method == 'GET':
        id = request.GET.get('category')  # get the query parameter
    try:
        Category_selected = Category.objects.get(id=id)
    except (Category.DoesNotExist, TypeError, ValueError):
        Category_selected = Category.objects.first()

    Community_data = Community.objects.filter(category=Category_selected)
    data = {
        'Community_data': Community_data,
        'Category_data': Category_data,
        'Category_selected': Category_selected
    }
    return render(request, 'community.html', data)

