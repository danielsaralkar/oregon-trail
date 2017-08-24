from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Family_Names(models.Model):
    user_id = models.ForeignKey(User)
    family1 = models.CharField(max_length=100, default="Friend 1")
    family2 = models.CharField(max_length=100, default="Friend 2")
    family3 = models.CharField(max_length=100, default="Friend 3")
    family4 = models.CharField(max_length=100, default="Friend 4")

    def _str_(self):
        return self.user_id

class Calamities(models.Model):
    calamity = models.CharField(max_length=100)
    action = models.CharField(max_length=100)

class Profession(models.Model):
    skills = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    money = models.DecimalField(max_digits=5, decimal_places=0)
    image = models.CharField(max_length=100)

class Supplies(models.Model):
    supply = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)