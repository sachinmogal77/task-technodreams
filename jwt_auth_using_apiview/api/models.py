from django.db import models

class Employee(models.Model):
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    city = models.CharField(max_length=30)
    contact_no = models.IntegerField()
    