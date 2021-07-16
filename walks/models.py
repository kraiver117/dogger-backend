from users.models import Profile
from walkers.models import Walker
from pets.models import Pet
from django.db import models

class Walk(models.Model):
    walker = models.ForeignKey(Walker, on_delete=models.CASCADE, default=1)

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)

    pet = models.ManyToManyField(Pet)

    beginning = models.DateTimeField(null=False, blank=False)
    end = models.DateTimeField(null=False, blank=False)

    is_accepted = models.BooleanField(default=False)

    is_finished = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Paseo por @{walker} con {pet}'.format(walker=self.walker, pet=self.pet)

