from django.db import models
from django.contrib.auth.models import User

# Create your models here.
''' 
django only gives this information about user by default:
    username
    password
    first_name
    last_name
    email

and if i want to extend this fields i should use one of the
following ways:
    1- proxy models
    2- One-to-One field -> the most used one
    3- Extend Abstract Base User
    4- Extend Abstarct User

and now we are gonna use One-to-One field 

by default we have User and we want to add our Profile
User + Profile
so i am gonna add them together by making a One-to-One
relationship between them
'''


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)
