from django.db import models


class Sabjimandi(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=2000, null=True, blank=True)
    created_date = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name