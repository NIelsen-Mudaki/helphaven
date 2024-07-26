from django.shortcuts import render, redirect
from .forms import AppointmentForm

def home(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = AppointmentForm()
    return render(request, 'home.html', {'form': form})

def success(request):
    return render(request, 'success.html', name='success')
