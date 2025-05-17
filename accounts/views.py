from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UserRegistrationForm
from .models import User

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    context = {
        'user': user,
    }
    template_name = 'accounts/patient_dashboard.html' if user.is_patient else 'accounts/doctor_dashboard.html'
    return render(request, template_name, context)
