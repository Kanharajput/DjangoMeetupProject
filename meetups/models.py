from django.db import models

# Create your models here.

# one to many , as many meetups can happen at same location
class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.address}"


class Meetup(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    slug = models.SlugField()
    image = models.ImageField(upload_to="images",null=True)       # upload images inside images folder inside MediaUploads folder
    place = models.ForeignKey(Location,on_delete=models.CASCADE,null=True)       # one to many
    
    def __str__(self):
        return self.title