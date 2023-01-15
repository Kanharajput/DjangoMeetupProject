from django.urls import path
from . import views

# add meetup in base url so removed from here
urlpatterns = [ 
    path("",views.index),      
    path("<slug:meetup_slug>",views.meetupDetail, name="meetup_detail")
]
