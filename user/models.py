from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name
