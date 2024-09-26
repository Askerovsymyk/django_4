


from django.urls import path
from .views import (DirectorListView,
                    DirectorDetailView,
                    MovieListView,
                    MovieDetailView,
                    ReviewListView,
                    ReviewDetailView,
                    MovieReviewView,
                    create_director,
                    modify_or_delete_director,
                    create_review,
                    create_movie,
                    modify_or_delete_movie,
                    modify_or_delete_review,)

urlpatterns = [
    path('directors/', DirectorListView.as_view(), name='director-list'),
    path('directors/<int:id>/', DirectorDetailView.as_view(), name='director-detail'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:id>/', MovieDetailView.as_view(), name='movie-detail'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:id>/', ReviewDetailView.as_view(), name='review-detail'),
    path('movies/reviews/', MovieReviewView.as_view(), name='movie-review'),

    path('api/v1/directors/', create_director, name='create_director'),
    path('api/v1/directors/<int:id>/', modify_or_delete_director, name='modify_or_delete_director'),

    path('api/v1/movies/', create_movie, name='create_movie'),
    path('api/v1/movies/<int:id>/', modify_or_delete_movie, name='modify_or_delete_movie'),

    path('api/v1/reviews/', create_review, name='create_review'),
    path('api/v1/reviews/<int:id>/', modify_or_delete_review, name='modify_or_delete_review'),
]
