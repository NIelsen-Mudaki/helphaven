from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import SignupForm

def index(request):
    return render(request, 'core/index.html')


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:   
        form = SignupForm()

    return render(request, 'core/signup.html', 
                  {'form':form}
                  )



def logout_view(request):
  """Logs out the current user and redirects to a specified page."""
  logout(request)
  # Optional: Redirect to a specific page after logout
  return HttpResponseRedirect("/")  # Change '/login/' to your desired URL
