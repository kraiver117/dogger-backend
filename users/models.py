# Django
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """User model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=10, blank=True)
    photo = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    is_owner = models.BooleanField(default=True)

    country = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        """Return username"""
        return self.user.username