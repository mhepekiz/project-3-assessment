from django.db import models
from django.urls import reverse

# Create your views here.
class Wacky(models.Model):
    item = models.CharField(max_length=50)
    quant = models.CharField(max_length=5)


    def __str__(self):
        return self.item
    def get_absolute_url(self):
        return reverse('index') 