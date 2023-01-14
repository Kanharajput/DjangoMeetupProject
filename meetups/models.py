from django.db import models

# Create your models here.

class Meetup(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    slug = models.SlugField()
    

    def __str__(self):
        return self.title