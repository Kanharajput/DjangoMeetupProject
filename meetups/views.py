from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # path till templates is known by django once we add app to installed apps
    return render(request,"meetups/index.html")    