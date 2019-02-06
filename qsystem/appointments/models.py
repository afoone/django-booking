from django.db import models
from swingtime.models import Occurrence

# Create your models here.

class Appointment(models.Model):
    dni = models.CharField(max_length = 16)
    email = models.EmailField()
    occurrence = models.ManyToManyField(Occurrence)

    # class Meta:
        # verbose_name = _('appointment')
        # verbose_name_plural = _('appointments')

    def __str__(self):
        return self.dni + " " + self.email