from django.db import models


class Restroom(models.Model):
    address = models.CharField(max_length=200)
