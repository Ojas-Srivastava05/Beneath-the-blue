from django.shortcuts import render,HttpResponse

# Create your views here.
def explore_map(request):
     return render(request,"explore_map.html")