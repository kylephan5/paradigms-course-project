from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = None
    last_name = None
    name = models.CharField(("name"), max_length=150, blank=True)

    def __str__(self):
        return self.username