from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # We can add fields like college_name here later
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
