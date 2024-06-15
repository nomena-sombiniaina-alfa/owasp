from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def profile(request, pk):
    template = 'idor/profile.html'
    profile = User.objects.get(pk=pk)
    context = {
        'profile': profile
    }
    return render(request,template , context)

def home(request):
    return render(request,'idor/home.html')

def login_user(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST.get('username'),
            password = request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect('idor:profile', pk=user.id, permanent=True)
    return render(request, 'idor/login.html')


class UserLoginView(LoginView):
    template_name = 'idor/login.html'
    success_url = reverse_lazy('idor:home')
    redirect_authenticated_user = True
    
class UserLogoutView(LogoutView):
    pass