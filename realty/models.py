from django.db import models

# Create your models here.
class Stu(models.Model):
    sname = models.CharField(max_length=30)


class Clazz(models.Model):
    cname = models.CharField(max_length=60)


class Han(models.Model):
    hname = models.CharField(max_length=60)
