from django.db import models

# Create your models here.

class Meetup(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    slug = models.SlugField()
    image = models.ImageField(upload_to="images",null=True)       # upload images inside images folder inside MediaUploads folder
    

    def __str__(self):
        return self.title