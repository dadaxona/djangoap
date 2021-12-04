from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')