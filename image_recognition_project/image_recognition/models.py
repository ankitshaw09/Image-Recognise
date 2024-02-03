from django.db import models

class RecognizedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    prediction = models.CharField(max_length=100)
