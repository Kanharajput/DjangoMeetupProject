from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = [
        {"title":"First Meetup"},
        {"title":"Second Meetup"}
    ]
    # always pass a single dictionary in render functions 
    # as there is only single dictionary acceptance is there 
    context = {
        "all_meetups":data,
        "show_meetups_data":False
    }
    return render(request,
                    "meetups/index.html",   
                        context)    