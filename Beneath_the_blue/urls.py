"""Beneath_the_blue URL Configuration"""
from django.contrib import admin
from django.urls import path
from home.views import *
from community.views import *
from ocean.views import *
# from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home")
    ,path('sign_in/',sign_in, name="sign_in")
    ,path('sign_up/',sign_up, name="sign_up")
    # ,path('logout/',logout, name="logout")
    ,path('community/',community_page, name="community_page"),
    path('explore_map/', explore_map, name="explore_map"),
    path('quiz/', quiz, name='quiz'),
    path('threats/', threats, name='threats'),
    # path('solutions/', solutions, name='solutions'),
    # path('threats_solution/', threats_solution, name='threats_solution'),
    path('endangered_species/', endangered_species, name='endangered_species'),
    path('submit-pledge/', submit_pledge, name='submit_pledge'),
    path('submit-idea/', submit_idea, name='submit_idea'),
    path('submit-feedback/', submit_feedback, name='submit_feedback'),
    path('subscribe/', subscribe, name='subscribe'),
    ]
