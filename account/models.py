from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


#Custom user model based on the django.contrib.auth.models.User with two additional fields
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    questions_list = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)

