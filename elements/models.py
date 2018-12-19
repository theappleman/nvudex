from django.db import models

class Element(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=12, unique=True)
