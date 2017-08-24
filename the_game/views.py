from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Family_Names, Calamities, Profession, Supplies


# Create your views here.
def main_page(request):
    return render(request, 'main.html', {"STATUS": "SUCCESS"})


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
            return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def home_page(request):
    if request.user.is_authenticated():
        current_user = request.user
        try:
            profession = Profession.objects.all()
            return render(request, 'home.html', {"status": "success","name":current_user, "professions":profession})
        except ObjectDoesNotExist as e:
            return render(request, 'home.html', {"status": "fail","name":current_user})
    else:
        return HttpResponseRedirect("/")