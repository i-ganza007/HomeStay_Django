from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    #username=None
    id = models.AutoField(primary_key=True)
    first_name = models.TextField(max_length=15)
    last_name = models.TextField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10,unique=True,blank=False,null=False)

    def __str__(self):
        return f'{self.first_name},{self.last_name}'
    
# When using Abstract User , register it in the Project settings file for it to work 