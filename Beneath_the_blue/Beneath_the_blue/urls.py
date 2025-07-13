from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.threats_solution, name='threats'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('quiz/', views.quiz, name='quiz'),
    path('summary/', views.summary, name='summary'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)