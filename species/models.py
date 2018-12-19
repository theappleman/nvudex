from django.db import models

class Species(models.Model):
    class Meta:
        verbose_name_plural = 'species'

    pokedex = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=20, unique=True)
    types = models.ManyToManyField('elements.Element')
