from django.db import models
from django.utils import timezone


class Oferta(models.Model):
    nazwa_firmy = models.CharField(max_length=100)
    branza = models.CharField(max_length=200)
    lokalizacja = models.CharField(max_length=100)
    wakat = models.CharField(max_length=100)
    wynagrodzenie = models.FloatField()
    opis = models.TextField()
    data_utworzenia = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.data_utworzenia = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwa_firmy