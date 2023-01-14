from django.urls import path
from . import views


urlpatterns = [
    path("meetups",views.index),
    path("meetups/<slug:slug>",views.meetupDetail, name="meetup_detail")

]
