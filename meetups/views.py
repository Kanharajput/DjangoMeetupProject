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