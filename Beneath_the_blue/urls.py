"""Beneath_the_blue URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from community.views import *
from ocean.views import *
from species.views import *
# from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home")
    ,path('sign_in/',sign_in, name="sign_in")
    ,path('sign_up/',sign_up, name="sign_up"),
    path('logout/',user_logout, name='logout')
    ,path('community/',community_page, name="community_page"),
    path('explore_map/',explore_map, name="explore_map"),
    path('quiz/', quiz, name='quiz'),
    path('next/', next_question, name='next_question'),
    
    path('threats/', threats, name='threats'),
    path('endangered_species/', endangered_species, name='endangered_species'),
    path('submit-pledge/', submit_pledge, name='submit_pledge'),
    path('submit-idea/', submit_idea, name='submit_idea'),
    path('submit-feedback/', submit_feedback, name='submit_feedback'),
    # path('subscribe/', Subscriber, name='subscribe'),
    path('CommunityPost/', community_posts, name='community_posts'),
    # path('community/',community_posts, name='community_posts'),
    path('create-post/', create_post, name='create_post'),
    path('my-posts/', my_posts, name='my_posts'),
    path('posts/<int:post_id>/edit/', edit_post, name='edit_post'),
    path('posts/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('posts/<int:post_id>/like/', like_post, name='like_post'),
    path('media/<int:media_id>/delete/', delete_media, name='delete_media'),
    path('add_comment/<int:post_id>/', add_comment, name='add_comment'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)