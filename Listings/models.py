import datetime
from django.db import models
from Users.models import User
from Homestay import settings
from django.db.models import CheckConstraint, Q , F

class BaseModel(models.Model):
    description = models.TextField(max_length=200,blank=False,default=None)
    price = models.PositiveIntegerField(blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        






class PropertyListing(models.Model):
    prop_name = models.CharField(max_length=20, unique=True, blank=True)  
    price = models.PositiveIntegerField(blank=False, null=False)
    description = models.CharField(max_length=200, blank=False)  
    location = models.CharField(max_length=15, blank=False, null=False)
    address = models.CharField(max_length=15)  
    is_urban = models.BooleanField(default=True)
    seen_listings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='seen_properties', blank=True)
    potential_interest = models.PositiveIntegerField(default=0)
    bedrooms = models.PositiveIntegerField(blank=False, null=False)  
    bathrooms = models.PositiveIntegerField(blank=False, null=False)  
    is_furnished = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.address:
            self.address = self.location  
        super().save(*args, **kwargs)



    def __str__(self):
        return f'{self.prop_name} at {self.price} in {self.location}'

def get_current_time():
    return datetime.datetime.now().time()

def get_default_time():
    return datetime.time()

class Event(models.Model):
    description = models.TextField(max_length=200, blank=False, default=None)
    event_name = models.TextField(max_length=20, unique=True, blank=True)
    price = models.PositiveIntegerField(blank=False, null=False)
    location = models.CharField(max_length=15)
    slots_available = models.PositiveIntegerField(blank=False, default=None)
    date = models.DateField(null=False, default=datetime.date.today)
    time_from = models.TimeField(default=get_current_time)
    time_to = models.TimeField(default=get_default_time)

    def __str__(self):
        return f'{self.event_name} at {self.price} in {self.location}'

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(price__gte=0),
                name='Non_negative_price'
            ),
            CheckConstraint(
                check=Q(date__gte=datetime.date.today()),
                name='Date_must_not_be_in_the_past'
            ),
            CheckConstraint(
                check=Q(time_to__gte=F('time_from')),
                name='Time_to_must_be_after_time_from'
            )
        ]
# You can't serialize a method directly like today and date , you have to use functions or it will be serialized like that 