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
    meetup_details = [
                {
                    "title":"first-meetup",
                    "description":"Description of first meetup",
                    "location":"Barda Punarwas",
                    "address":"Kanha's Plot",
                    "slug":"first-meetup"
                },
                {
                    "title":"second-meetup",
                    "description":"Description of second meetup",
                    "location":"Bakaner",
                    "address":" Mohit's Shop",
                    "slug":"second-meetup"
                }
    ]

    # find the dictionary which having the slug passed by user
    for dict in meetup_details:
        if dict["slug"] == slug:
            meetup_detail = dict

    return render(request,"meetups/meetup-details.html",{"meetup_detail":meetup_detail})
