
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return 'Image: ' + self.name


class Tipology(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return 'Image: ' + self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    detail = models.CharField(max_length=1000)
    place = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    creation_date = models.DateTimeField(null=False, auto_now_add=True)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    category_type = models.ForeignKey(Category, blank=False, null=False, on_delete=models.CASCADE)
    event_type = models.ForeignKey(Tipology, blank=False, null=False, on_delete=models.CASCADE)
    creation_user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return 'Image: ' + self.name