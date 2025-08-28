from rest_framework.authtoken import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as custom_views
router = DefaultRouter()
router.register('register', custom_views.RegistrationViewSet, basename='register')
 
urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('logout/', custom_views.LogoutView.as_view()),
    path('', include(router.urls)),
]