from django.db import models
from Users.models import User

class BaseModel(models.Model):
    description = models.TextField(max_length=200,blank=False,default=None)
    price = models.PositiveIntegerField(blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        


class PropertyListing(BaseModel):
    prop_name = models.TextField(max_length=20,unique=True,blank=True)
    price = models.PositiveIntegerField(blank=False,null=False)
    description = models.TextField(max_length=200,blank=False,default=None)
    location = models.TextField(max_length=15,blank=False,null=False)
    address = models.CharField(max_length=15,default=f'{location}')
    is_urban = models.BooleanField(default=True)
    potential_interest = models.PositiveIntegerField(default=0)
    bedrooms = models.PositiveIntegerField(blank=False,default=None)
    bathrooms = models.PositiveIntegerField(blank=False,default=None)
    is_furnished = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.prop_name} at {self.price} in {self.location}'

class Event(BaseModel):
    description = models.TextField(max_length=200,blank=False,default=None)
    event_name = models.TextField(max_length=20,unique=True,blank=True)
    price = models.PositiveIntegerField(blank=False,null=False)
    location = models.CharField(max_length=15)
    slots_available = models.PositiveIntegerField(blank=False,default=None)

    def __str__(self):
        return f'{self.event_name} at {self.price} in {self.location}'


