from django.db import models

# Create your models here.

# one to many , as many meetups can happen at same location
class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.address}"


class Participants(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Participants"


class Organizer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Meetup(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    slug = models.SlugField()
    image = models.ImageField(upload_to="images",null=True)       # upload images inside images folder inside MediaUploads folder
    date_time = models.DateTimeField(auto_now=True)
    place = models.ForeignKey(Location,on_delete=models.CASCADE,null=True)       # one to many
    participants = models.ManyToManyField(Participants)       # doesn't need to set on_delete and null=True in many to many fields
    organizer = models.OneToOneField(Organizer,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.title