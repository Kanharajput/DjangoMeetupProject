from django.contrib import admin
from .models import Meetup,Location,Participants,Organizer
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    prepopulated_fields = {
            "slug" : ["title"]            
    }

admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participants)
admin.site.register(Organizer)