from django.db import models

# Create your models here.
class Stu(models.Model):
    sname = models.CharField(max_length=30)