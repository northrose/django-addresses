from django.db import models

class State(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=2)

    def __unicode__(self):
        return self.name
