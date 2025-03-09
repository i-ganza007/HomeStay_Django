from django.db import models
from Users.models import User
from Homestay import settings

class BaseModel(models.Model):
    description = models.TextField(max_length=200,blank=False,default=None)
    price = models.PositiveIntegerField(blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        


from django.contrib.auth.models import User
from django.db import models

class PropertyListing(models.Model):
    prop_name = models.CharField(max_length=20, unique=True, blank=True)  # Changed to CharField
    price = models.PositiveIntegerField(blank=False, null=False)
    description = models.CharField(max_length=200, blank=False)  # Changed to CharField
    location = models.CharField(max_length=15, blank=False, null=False)
    address = models.CharField(max_length=15)  # Removed default=f'{location}'
    is_urban = models.BooleanField(default=True)
    seen_listings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='seen_properties', blank=True)
    potential_interest = models.PositiveIntegerField(default=0)
    bedrooms = models.PositiveIntegerField(blank=False, null=False)  # Removed default=None
    bathrooms = models.PositiveIntegerField(blank=False, null=False)  # Removed default=None
    is_furnished = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.address:
            self.address = self.location  # Dynamically set address if not provided
        super().save(*args, **kwargs)



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


