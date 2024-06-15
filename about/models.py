# Importing required libraries required to build models

from django.db import models


# Create About model
class About(models.Model):
    """
    Stores single about us requrest.
    """
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


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

# Create faq model
class Faq(models.Model):
    """
    Stores single about us requrest.
    """
    query = models.CharField(max_length=500, unique=True)
    answer = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.query}"
