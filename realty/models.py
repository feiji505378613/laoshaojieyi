from django.db import models

# Create your models here.
class Stu(models.Model):
    sname = models.CharField(max_length=30)


class Clazz(models.Model):
    cname = models.CharField(max_length=60)



class h(models.Model):
    tname = models.CharField(max_length=60)


class Hello(models.Model):
    hname = models.CharField(max_length=30)
    age = models.CharField(max_length=1)


