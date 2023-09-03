
from django.shortcuts import render
from django.http import HttpResponse

# def Welcome(request):
#     return HttpResponse("Hi, this is my first Django Project")

def Welcome(request):
    return render(request, "index.html")

def User(request):
    username = request.GET['username']
    print(username)
    return render(request, "user.html", {'name' : username})

# Create your views here.

# django:  MVT (Model View Template)
# Java: MVC (Model View Controller)

# basicConcept is samll app to run the any function we've to link this to original project djangoMLDeploymnet
