from django.db import models

# Create your models here.

class About(models.Model):
    about = models.TextField(max_length=1000000)
    image = models.ImageField(null=True,default='')
    vision = models.TextField(max_length=1000000)
    image2 = models.ImageField(null=True,default='')
    mission1 = models.TextField(max_length=200)
    mission2 = models.TextField(max_length=200)
    mission3 = models.TextField(max_length=200)
    mission4 = models.TextField(max_length=200)

class Gallerie(models.Model):
    image = models.ImageField(null=True,default='')

class Message(models.Model):
    name  = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1000000)

class Principal(models.Model):
    image = models.ImageField()
    speech = models.TextField(max_length=150)

class Founder(models.Model):
    image = models.ImageField()
    speech = models.TextField(max_length=150)

class VicePrincipal(models.Model):
    image = models.ImageField()
    speech = models.TextField(max_length=150)