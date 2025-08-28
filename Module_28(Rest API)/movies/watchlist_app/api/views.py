from watchlist_app import models
from .import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status  
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets
from .import permissions
import django_filters.rest_framework
from .import pagination

# @api_view()
# def movie_list(request):
#     movies = models.MovieList.objects.all()# python model
#     serializer = serializers.MovieListSerializer(movies, many =True) #python object ke json e convert korbe
#     return Response(serializer.data)
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = models.MovieList.objects.all()# python model
#         serializer = serializers.MovieListSerializer(movies, many =True) #python object ke json e convert korbe
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = serializers.MovieListSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET','PUT','PATCH','DELETE'])
# #PUT--> Update reqest(whole object kei pathate hoy)
# #PATCH--> ja part change korbo just seta te pathalei hobe
# def movie_detail(request,pk):
#     movie = get_object_or_404(models.MovieList, pk =pk )

#     if request.method == 'GET':
#         serializer = serializers.MovieListSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         serializer = serializers.MovieListSerializer(movie, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == 'PATCH':
#         serializer = serializers.MovieListSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response({'message' : 'Movie deleted successfully'})
    
#class based view
# # 1. List of all movies , Create a new movie
# class MovieListCreateView(generics.ListCreateAPIView):
#     queryset = models.MovieList.objects.all()
#     serializer_class = serializers.MovieListSerializer

# #2. Single movie/update/delete
# class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.MovieList.objects.all()
#     serializer_class = serializers.MovieListSerializer

# #3. Create a new review
# class ReviewListCreateView(generics.CreateAPIView):
#     queryset = models.Reviews.objects.all()
#     serializer_class = serializers.ReviewSerializer

# #4. Single review/update/delete
# class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Reviews.objects.all()
#     serializer_class = serializers.ReviewSerializer 



class MovieListViewSet(viewsets.ModelViewSet):
    queryset = models.MovieList.objects.prefetch_related('reviews') #m2m, reverse foreign key relation
    serializer_class = serializers.MovieListSerializer
    pagination_class = pagination.MoviePageNumberPagination

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Reviews.objects.select_related('movie')  # Use select_related for foreign key relations
    serializer_class = serializers.ReviewSerializer
    permission_classes= [ permissions.IsReviewerOrReadOnly,IsAuthenticated]  # Ensure that only authenticated users can create reviews
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['reviewer__username', 'rating']
