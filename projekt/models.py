from django.db import models
from django.utils import timezone

class Firma(models.Model):
    nazwa_firmy = models.CharField(max_length=100,)
    miasto = models.CharField(max_length=100)
    ulica = models.CharField(max_length=100)
    telefon = models.CharField(max_length=9)
    email = models.CharField(max_length=30)


class Oferta(models.Model):
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE)
    branza = models.CharField(max_length=200)
    lokalizacja = models.CharField(max_length=100)
    wakat = models.CharField(max_length=100, blank = True)
    wynagrodzenie = models.FloatField(default=0, blank=True)
    opis = models.CharField(max_length=1000)
    data_utworzenia = models.DateTimeField(
            default=timezone.now)

'''
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
'''