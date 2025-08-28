from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    car_models = models.CarModel.objects.all()
    car_details = []
    for car in car_models:
        car_details.append({
            'car_name': car.name,
            'car_company': car.car_company.name,
            'ceo_name': models.Ceo.objects.filter(car_company= car.car_company).first(),
            'fule_names': [fule.name for fule in models.FuelType.objects.filter(car_models = car)],
        })
    return render(request,'cars/home.html', {'car_details': car_details})

