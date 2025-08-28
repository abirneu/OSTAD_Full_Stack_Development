from django.urls import path, include
from .import views # same folder er vitor tai .import
from rest_framework.routers import DefaultRouter
# eta asole kaj kore router er moto
#router er moto antena thakbe main body thakbe
router = DefaultRouter()
# Register your viewsets here
router.register('movies', views.MovieListViewSet, basename='movielist')
router.register('reviews', views.ReviewViewSet, basename='review') 
urlpatterns = [
    # path('', views.MovieListCreateView.as_view()),
    # path('<pk>/', views.MovieDetailView.as_view()),
    # path('reviews/', views.ReviewListCreateView.as_view()),
    # path('reviews/<pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('', include(router.urls)),  # Include the router's URLs

]
