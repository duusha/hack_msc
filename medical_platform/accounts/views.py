from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # After saving the form, authenticate and log the user in
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Ensure this is password1 as it's the first password field
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('auth')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def auth_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_panel')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/auth.html', {'form': form})

def admin_panel(request):
    users = CustomUser.objects.all()
    return render(request, 'accounts/admin_panel.html', {'users': users})

