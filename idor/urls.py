from django.urls import path
from . import views

app_name = 'idor'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]