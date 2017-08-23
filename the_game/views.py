from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

# Create your views here.
def home_page(request):
    # return HttpResponse("You're looking at question")
    if request.user.is_authenticated():
        return render(request, 'home.html', {"STATUS": "SUCCESS"})
    else:
        return HttpResponseRedirect("/login")


# Register / Sign-Up to the website
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})