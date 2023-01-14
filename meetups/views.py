from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup

# Create your views here.
def index(request):
    meetups = Meetup.objects.all()      # access all the meetups from database
    return render(request,"meetups/index.html",{"all_meetups": meetups})    


def meetupDetail(request,meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)   # fetch the meetup from the database
    return render(request,"meetups/meetup-details.html",{"meetup_detail":meetup})
