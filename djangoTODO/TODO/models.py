from django.db import models
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    contex=models.CharField(max_length=255)
    title=models.CharField(max_length=30)
    date=models.DateTimeField(default=timezone.now)
    zrobione=models.BooleanField(default=True)
    
    def __str__(self)->str:
        return self.title
