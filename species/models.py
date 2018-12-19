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

    @property
    def single_type(self):
        if self.types.count() <= 1:
            return True

    def double_damage(self):
        if self.single_type:
            return self.types.first().weak_against()

        e1 = self.types.first()
        q1 = e1.weak_against()

        e2 = self.types.last()
        q2 = e2.weak_against()

        return q1.intersection(q2)

    def single_damage(self):
        if self.single_type:
            return self.types.first().weak_against()

        e1 = self.types.first()
        q1 = e1.weak_against()

        e2 = self.types.last()
        q2 = e2.weak_against()

        return q1.union(q2)
