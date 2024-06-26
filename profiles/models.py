# Import required libraries to configure model

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from django_countries.fields import CountryField


# definiation to validate phone number
def validate_phone_number(value):
    """
    Custom validator for phone numbers.
    Validates that the phone number contains only digits
    and has a specific length.
    """
    # Remove any non-digit characters (e.g., spaces, dashes)
    cleaned_value = ''.join(filter(str.isdigit, value))

    # Check if the cleaned value has the desired length (e.g., 10 digits)
    if len(cleaned_value) != 10:
        raise ValidationError('Phone number must be numeric & 10 digits long!')

    # If everything is valid, return True
    return True


# Create UserProfile model
class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
            max_length=10,
            validators=[validate_phone_number],
            null=True,
            blank=True
        )
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


# definiation to create_or_update_user_profile
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
