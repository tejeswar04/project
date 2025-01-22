from django.db import models

# Create your models here.
class events(models.Model):
    title=models.CharField(blank=False,max_length=100,unique=True)
    img=models.URLField()
    des=models.TextField()
    link=models.URLField(blank=False)
    type=models.CharField(blank=False,max_length=100)