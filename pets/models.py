from users.models import Profile
from django.contrib.auth.models import User
from django.db import models

class Pet(models.Model):
    """Pet model"""
    big = 'Grande'
    medium = 'Mediano'
    small = 'Pequeño'

    sizes = (
        (big, "Grande"),
        (medium, "Mediano"),
        (small, "Pequeño")
    )

    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    
    name = models.CharField(max_length=50, null=False, blank=False)
    size = models.CharField(max_length=20, choices=sizes, null=True, blank=True)
    photo = models.ImageField(upload_to='pets/pictures', null=True, blank=True)
    extra_info = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        """Return name"""
        return self.name
        
