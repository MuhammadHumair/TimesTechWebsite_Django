from django.db import models

# Create your models here.


class enquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.IntegerField()
    subject = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    status = models.BooleanField()
