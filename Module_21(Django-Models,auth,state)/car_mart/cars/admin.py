from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.CarCompany)
admin.site.register(models.Ceo)
admin.site.register(models.CarModel)
admin.site.register(models.FuelType)

