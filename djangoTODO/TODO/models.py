from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Task(models.Model):
    contex=models.CharField(max_length=255)
    title=models.CharField(max_length=30)
    date=models.DateTimeField(default=timezone.now)
    zrobione=models.BooleanField(default=True)
    
    def __str__(self)->str:
        return self.title

    def get_absolute_url(self):
        return reverse('TODO-POSTS')    