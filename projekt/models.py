from django.db import models
from django.utils import timezone


class Firma(models.Model):
    nazwa_firmy = models.CharField(max_length=100, default='SOME_NAZWA_FIRMY')
    miasto = models.CharField(max_length=100)
    ulica = models.CharField(max_length=100)
    telefon = models.CharField(max_length=9)
    email = models.CharField(max_length=30)

    def publish(self):
        self.data_utworzenia = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwa_firmy


class Oferta(models.Model):
    branza = models.CharField(max_length=200)
    lokalizacja = models.CharField(max_length=100)
    wakat = models.CharField(max_length=100, blank = True)
    wynagrodzenie = models.FloatField(default=0, blank=True)
    opis = models.CharField(max_length=1000)
    wiek_dol = models.IntegerField(default=18)
    wiek_gora = models.IntegerField(default=30)
    data_utworzenia = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.data_utworzenia = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwa_firmy

