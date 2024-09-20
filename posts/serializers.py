


from rest_framework import serializers
from .models import Director, Movie, Review
from django.db.models import Avg


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = ['id', 'name', 'birth_date']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name field cannot be empty.")
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return value

    def validate_birth_date(self, value):
        if not value:
            raise serializers.ValidationError("Birth date cannot be empty.")
        if value.year < 1900:
            raise serializers.ValidationError("Birth date must be after 1900.")
        return value

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'director']

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        if len(value) < 1:
            raise serializers.ValidationError("Title must be at least 1 character long.")
        return value

    def validate_release_date(self, value):
        if not value:
            raise serializers.ValidationError("Release date is required.")
        if value.year < 1888:  # The year of the first film
            raise serializers.ValidationError("Release date must be after 1888.")
        return value

    def validate_director(self, value):
        if not value:
            raise serializers.ValidationError("Director is required.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie', 'review_text', 'rating', 'created_at']

    def validate_review_text(self, value):
        if not value:
            raise serializers.ValidationError("Review text cannot be empty.")
        if len(value) < 10:
            raise serializers.ValidationError("Review text must be at least 10 characters long.")
        return value

    def validate_rating(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError("Rating must be between 1 and 10.")
        return value

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

