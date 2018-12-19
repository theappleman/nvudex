from django.db import models

class Damage(models.Model):
    damage = models.ForeignKey('elements.Element', related_name="damage")
    target = models.ForeignKey('elements.Element', related_name="target")
    factor = models.IntegerField()
