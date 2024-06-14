from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import CustomUserCreationForm, ScheduleForm
from .models import CustomUser, Schedule
from datetime import datetime, timedelta

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            form.save_m2m()
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
                return redirect('user_schedule', user_id=user.id)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/auth.html', {'form': form})

@login_required
def admin_panel(request):
    if not request.user.admin:
        return HttpResponseForbidden("You are not authorized to access this page.")
    users = CustomUser.objects.all()
    return render(request, 'accounts/admin_panel.html', {'users': users})

@login_required
def user_schedule(request, user_id):
    if request.user.id != user_id:
        return HttpResponseForbidden("You are not authorized to access this page.")
    user = get_object_or_404(CustomUser, id=user_id)
    today = datetime.today()
    current_week = request.GET.get('week', 0)
    try:
        current_week = int(current_week)
    except ValueError:
        current_week = 0
    start_of_week = today + timedelta(weeks=current_week, days=-today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    schedules = user.schedules.filter(date__range=[start_of_week, end_of_week])

    days = [(start_of_week + timedelta(days=i)).date() for i in range(7)]
    week_schedules = {day: [] for day in days}
    for schedule in schedules:
        week_schedules[schedule.date].append(schedule)

    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.user = user
            schedule.save()
            return redirect('user_schedule', user_id=user_id)
    else:
        initial_data = {
            'date': datetime.today().date(),
            'time_from': (datetime.now() + timedelta(hours=1)).time().strftime("%H:%M"),
            'time_to': (datetime.now() + timedelta(hours=2)).time().strftime("%H:%M"),
            'description': 'Общее собрание'
        }
        form = ScheduleForm(initial=initial_data)
    return render(request, 'accounts/user_schedule.html', {'user': user, 'week_schedules': week_schedules, 'form': form, 'current_week': current_week})

@login_required
def all_schedules(request):
    if not request.user.admin:
        return HttpResponseForbidden("You are not authorized to access this page.")
    
    today = datetime.today()
    current_week = request.GET.get('week', 0)
    try:
        current_week = int(current_week)
    except ValueError:
        current_week = 0
    start_of_week = today + timedelta(weeks=current_week, days=-today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    schedules = Schedule.objects.filter(date__range=[start_of_week, end_of_week]).select_related('user')

    days = [(start_of_week + timedelta(days=i)).date() for i in range(7)]
    week_schedules = {day: [] for day in days}
    for schedule in schedules:
        week_schedules[schedule.date].append(schedule)

    context = {
        'week_schedules': week_schedules,
        'current_week': current_week
    }
    return render(request, 'accounts/all_schedules.html', context)

