from django.db import models

class Element(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=12, unique=True)

    def effective(self):
        return self.damage.exclude(factor__gt=100).order_by('-factor')

    def resists(self):
        return self.target.filter(factor__lt=100).order_by('factor')

    def weak_against(self):
        return self.target.filter(factor__gt=100).order_by('factor')
