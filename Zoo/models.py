from django.db import models


class Unique(models.Model):
    CHOICES = (
        ('Animal', "Animal"),
        ('Feed', "Feed"),
        ('Related Product', "Related Product"),

    )
    name = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self):
        return self.name


class NotUnique(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    marker_A = models.ForeignKey(Unique, on_delete=models.CASCADE)
    marker_B = models.ManyToManyField(NotUnique)

    def __str__(self):
        return self.name
