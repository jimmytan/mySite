__author__ = 'wenjuntan'

from django.db import models

class TripInfo (models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    country = models.CharField(max_length= 200, default='China')
    province = models.CharField(max_length= 200)
    city = models.CharField(max_length= 200)
    comments = models.TextField(blank = True)

    class Meta:
        ordering = ('created',)
