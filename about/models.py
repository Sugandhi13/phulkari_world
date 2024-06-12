# Importing required libraries required to build models

from django.db import models
from django.contrib.auth.models import User


# Create Contact model
class Contact(models.Model):
    """
    Stores single contact us requrest.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
