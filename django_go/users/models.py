from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER = (
        ('MEN','Men'),
        ('WOMEN','Women')
    )

    gender = models.CharField(max_length=20, choices=GENDER, null= True)
    age = models.IntegerField(null= True)
    access_key = models.CharField(max_length=20)




