from django.db import models

# Create your models here.
class univs(models.Model):
    name = models.CharField(blank=False, max_length=100, unique=True)
    img = models.URLField()
    location = models.CharField(blank=False, max_length=100)
    acceptance = models.CharField(blank=False, max_length=100)
    gre = models.CharField(blank=False, max_length=100)

class ranks(models.Model):
    name = models.ForeignKey(univs, on_delete=models.CASCADE)
    country = models.CharField(max_length=15, blank=False)
    topic = models.CharField(max_length=15, blank=False)
    score = models.FloatField(blank=False)
