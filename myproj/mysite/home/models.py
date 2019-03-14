from django.db import models

# Create your models here
class details(models.Model):
    name =models.CharField(max_length=250)
    contact =models.CharField(max_length=15)
    subject =models.CharField(max_length=250)
    message =models.CharField(max_length=1000)

    def __str__(self):
        return self.name
