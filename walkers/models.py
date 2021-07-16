from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Walker(models.Model):
    """User model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=10, blank=True)
    photo = models.ImageField(upload_to='walkers/pictures', blank=True, null=True)

    is_walker = models.BooleanField(default=True)

    current_walks = models.PositiveIntegerField(validators=[MaxValueValidator(3)] ,default=0)

    def __str__(self):
        """Return username"""
        return self.user.username