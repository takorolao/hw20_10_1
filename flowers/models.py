from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Bouquet(models.Model):
    name = models.CharField(max_length=100)
    flowers = models.ManyToManyField(Flower)

    def __str__(self):
        return self.name
