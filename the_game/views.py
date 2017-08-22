from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    # return HttpResponse("You're looking at question")
    return render(request, 'login.html', {"STATUS": "SUCCESS"})
