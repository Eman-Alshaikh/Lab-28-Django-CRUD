 
# Create your models here.

# user :  name=admin
# pass: 123456
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

class Snack(models.Model):
    title=models.CharField(max_length=255)
    purchaser =models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description =models.TextField(default='')
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_snack',kwargs={"pk":self.pk})
