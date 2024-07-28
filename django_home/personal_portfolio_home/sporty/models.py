from django.db import models


class Sporty(models.Model):
    section = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='sporty/images/')
    url = models.URLField(blank=True)
