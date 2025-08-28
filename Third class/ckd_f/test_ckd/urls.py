from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    # path('predict/', views.predict, name='predict'),
    path('doctor_dashboard/', login_required(views.doctor_dashboard), name='doctor_dashboard'),
    path('patient_info_id/', login_required(views.patient_info_id), name='patient_info_id'),
    path('patient/<str:phone>/', views.patient_profile, name='patient_profile'),
]