from django.db import models
try:
    from djangae.fields import RelatedSetField as ManyToManyField
except ImportError:
    from django.db.models import ManyToManyField

class Species(models.Model):
    class Meta:
        verbose_name_plural = 'species'

    pokedex = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=20, unique=True)
    types = ManyToManyField('elements.Element')
