from django.db import models


class Habit(models.Model):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=49)
    created = models.DateField(auto_now_add=True)
