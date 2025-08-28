from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('home/',views.home, name="home"), 
    
    path('create/', views.create_student, name="create_student"),
    path('edit/<int:id>/', views.update_student, name="update_student"),
    path('delete/<int:id>/', views.delete_student, name="delete_student"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('profile/', views.user_profile, name="user_profile"),



]
