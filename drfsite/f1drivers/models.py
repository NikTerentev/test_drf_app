from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Racer(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    nationality = models.CharField(max_length=255)
    biography = models.TextField(blank=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name
