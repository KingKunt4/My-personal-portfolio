from django.db import models
class devices(models.Model):
    device = models.CharField(max_length= 20)
    location= models.CharField(max_length= 20)