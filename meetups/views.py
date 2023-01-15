from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup
from .forms import RegistrationForm

# Create your views here.
def index(request):    
    meetups = Meetup.objects.all()      # access all the meetups from database
    return render(request,"meetups/index.html",{"all_meetups": meetups})    
    


def meetupDetail(request,meetup_slug):
    # for hanling both post and get request we need it
    meetup = Meetup.objects.get(slug=meetup_slug)   # fetch the meetup from the database

    if request.method == "POST":      # if post means it have form data
        # initiate the form 
        user_entered_form = RegistrationForm(request.POST)    # it will automatically fetch the entries

        if user_entered_form.is_valid():         # check is it valid if valid then
            partictipant = user_entered_form.save()    # save the participants data
            partictipant.meetup.add(meetup)                  # add this participant for the meetup
            partictipant.save()             # save this data to database it know about database because it is created using that
            context = {
                "meetup_detail":meetup,
                "registered":"You are registered now"     # send back user to the same page but with registration info
            }
            return render(request,"meetups/meetup-details.html",context)


    # below code is for get request
    new_form = RegistrationForm()

    
    return render(request,"meetups/meetup-details.html",{"meetup_detail":meetup,"form":new_form})

