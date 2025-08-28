from rest_framework import serializers
from watchlist_app import models

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField()  # Use StringRelatedField to show the username
    class Meta:
        model = models.Reviews
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Add this line
    # reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review_detail')  # Add this line
    # reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review_detail')  # Add this line


    class Meta:
        model = models.MovieList
        # fields = ['id', 'name', 'description', 'active', 'reviews']  # Add 'reviews' here
        fields = '__all__'