from django.db import models

class Element(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=12, unique=True)

    # Attacker
    def effective(self):
        return self.damage.exclude(factor__gt=100).order_by('-factor')

    def resisted(self):
        return self.damage.filter(factor__lt=100).order_by('factor')

    # Defender
    def resistant(self):
        return self.target.exclude(factor__lt=100).order_by('-factor')

    def weak_against(self):
        return self.target.filter(factor__gt=100).order_by('factor')
