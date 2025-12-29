from django.db import models

# Create your models here.
class Student(models.Model):
    # id = models.AutoField()                               # pk, added automatically by django
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    image = models.ImageField()
    file = models.FileField()
    date = models.DateField()

class Project(models.Model):
    pass