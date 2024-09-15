


from rest_framework import serializers
from .models import Director, Movie, Review
from django.db.models import Avg


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']

    def get_movies_count(self, obj):
        return obj.movies.count()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director', 'reviews', 'rating']

    def get_rating(self, obj):
        # Вычисление среднего рейтинга для каждого фильма
        return obj.reviews.aggregate(Avg('stars'))['stars__avg']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'