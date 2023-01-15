from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup,Participants
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
            username = user_entered_form.cleaned_data["name"]    # save the participants data
            # was_created is variable , it store the boolean value created or not
            registered_user,was_created = Participants.objects.get_or_create(name=username)   
            registered_user.meetup.add(meetup)
            # right now we have to add participants with meetup if participants is now or not it dosn't matter
            # but to show case this feature i am writing here
            #if was_created:
                #meetup.participants.add(registered_user)
                

            context = { 
                "meetup_detail":meetup,
                "registered":"You are now registered for this meetup"     # send back user to the same page but with registration info
            }
            return render(request,"meetups/meetup-details.html",context)


    # below code is for get request
    new_form = RegistrationForm()
    registered_users = meetup.participants.all()      # get all the registered users
    
    context = {
        "meetup_detail":meetup,
        "form":new_form,
        "participants":registered_users
    }
    return render(request,"meetups/meetup-details.html",context)

