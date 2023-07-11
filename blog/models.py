from django.db import models

# Create your models here.
from django.db import models
from django.contrib.gis.db import models


from django.contrib.gis.db import models

class Polygone(models.Model):
    nom = models.CharField(max_length=100)
    coordonnees = models.PolygonField()

    def __str__(self):
        return self.nom

