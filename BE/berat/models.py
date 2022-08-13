from django.db import models

# Create your models here.
 
class Berat(models.Model):
    tanggal = models.DateField()
    berat_max = models.PositiveIntegerField()
    berat_min = models.PositiveIntegerField()