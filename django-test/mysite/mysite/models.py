from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year = models.IntegerField()
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.make + ' ' + self.carmodel + ' ' + str(self.year) + ' ' + self.location + ' ' + self.status


class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.make + ' ' + self.carmodel


class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    branch = models.IntegerField()

    def __str__(self):
        return self.make + ' ' + self.carmodel
