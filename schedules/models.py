from django.db import models
from django.db.models.deletion import CASCADE
from walkers.models import Walker

class Schedule(models.Model):
    """Walker Schedule"""

    big = 'Grande'
    medium = 'Mediano'
    small = 'Pequeño'

    sizes = (
        (big, "Grande"),
        (medium, "Mediano"),
        (small, "Pequeño")
    )

    monday = 'Lunes'
    tuesday = 'Martes'
    wednesday = 'Miércoles'
    thursday = 'Jueves'
    friday = 'Viernes'
    saturday = 'Sábado'
    sunday = 'Domingo'

    days_of_week = (
        (monday, 'Lunes'),
        (tuesday, 'Martes'),
        (wednesday, 'Miércoles'),
        (thursday, 'Jueves'),
        (friday, 'Viernes'),
        (saturday, 'Sábado'),
        (sunday, 'Domingo'),
    )

    walker = models.ForeignKey(Walker, on_delete=CASCADE)

    beginning = models.TimeField( null=False, blank=False)
    end = models.TimeField(null=False, blank=False)

    day = models.CharField(max_length=10, choices=days_of_week)

    size_dog = models.CharField(max_length=20, choices=sizes, null=False, blank=False)