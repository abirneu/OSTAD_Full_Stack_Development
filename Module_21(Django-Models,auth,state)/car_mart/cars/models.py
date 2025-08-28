from django.db import models

# Create your models here.

#One to one relationship
#Car Company and CEO

class CarCompany(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ceo(models.Model):
    name = models.CharField(max_length=100)
    car_company = models.OneToOneField(CarCompany, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    car_company = models.ForeignKey(CarCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# ForeginKey --> Many to One

class FuelType(models.Model):
    name = models.CharField(max_length=100)
    car_models = models.ManyToManyField(CarModel)

    def __str__(self):
        return self.name