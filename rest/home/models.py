from django.db import models

# Create your models here.

class Employees(models.Model):
    firstname = models.CharField(max_length=12)
    lastname = models.CharField(max_length=12)


    def __str__(self):
        return self.firstname