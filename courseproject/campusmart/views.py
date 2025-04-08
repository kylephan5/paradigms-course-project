from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, UserLoginForm
# Create your views here.

def index(request):
    return render(request, 'campusmart/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log in the user after registration
            return redirect('campusmart:index')
    else:
        form = UserCreationForm()

    return render(request, 'campusmart/register.html', {'form': form})

def login(request):
    error_message = None
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            # Retrieve the authenticated user and log in.
            user = form.get_user()
            auth_login(request, user)
            # Check if there's a next parameter in the URL
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('campusmart:index')
        else:
            error_message = "The username/password combination does not match our records."
    else:
        form = UserLoginForm()
    return render(request, 'campusmart/login.html', {'form': form, 'error': error_message})

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('campusmart:index')

@login_required
def profile(request):
    # This is a placeholder for a profile view
    return render(request, 'campusmart/profile.html')