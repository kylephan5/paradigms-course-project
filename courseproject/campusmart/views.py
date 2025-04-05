from django.shortcuts import render, redirect
from .forms import UserCreationForm
# Create your views here.

def index(request):
    print(request)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'campusmart/register.html', {'form': form})

def login(request):
    # For Lang to do
    # might want to look at forms.py, create a login form similar to how I created a UserCreationForm. good for readability and reusability
    pass
