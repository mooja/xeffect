import os
import random

from string import ascii_lowercase, digits

from django.db import models


class Habit(models.Model):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=49)
    created = models.DateField(auto_now_add=True)

    @classmethod
    def create(cls, title):
        random.seed(os.urandom(20))

        id = ''.join(random.choice(ascii_lowercase + digits) for _ in range(20))
        status = '0'*49

        habit = cls(id=id, title=title, status=status)
        habit.save()
        return habit
