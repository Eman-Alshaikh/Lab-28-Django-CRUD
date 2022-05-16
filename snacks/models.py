from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Snack(models.Model):
    title=models.CharField(max_length=255)
    purchaser =models.CharField(max_length=255)
    description =models.CharField(max_length=255)
    

    def __str__(self):
        return self.title
    
