from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    meetups_data = [
            {
                "title":"First Meetup",
                "location":"Barda Punarwas",
                "slug":"first-meetup"
            },
            {
                "title":"Second Meetup",
                "location":"Bakaner",
                "slug":"second-meetup"
            }
        ]
    # always pass a single dictionary in render functions 
    # as there is only single dictionary acceptance is there 
    context = {
        "all_meetups":meetups_data,
        "show_meetups_data":False
    }
    return render(request,
                    "meetups/index.html",   
                        context)    


def meetupDetail(request,slug):
    meetup_details = {
        "first-meetup":"This page will show the details of first meetup",
        "second-meetup":"This page will show the details of second meetup"
    }
    meetup_detail = meetup_details[slug]
    return HttpResponse(meetup_detail)
