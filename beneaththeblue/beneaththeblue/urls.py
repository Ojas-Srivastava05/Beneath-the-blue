"""
URL configuration for beneaththeblue project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ocean import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('submit-pledge/', views.submit_pledge, name='submit_pledge'),
    path('submit-idea/', views.submit_idea, name='submit_idea'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('posts/', views.posts, name='posts'),
      path('explore-map/', views.explore_map, name='explore_map'),
       path('threats/', views.threats_view, name='threats'), 
       path('community/', views.community_page, name='community_page'), 
       path('quiz/', views.quiz_view, name='quiz'),
path('endangered-species/', views.endangered_species, name='endangered_species'),
]
