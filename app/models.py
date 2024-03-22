from django.db import models

class MyModel(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField(max_length=1000)
    
    