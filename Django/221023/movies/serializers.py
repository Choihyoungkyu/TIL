from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name', )

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview', )
        read_only_fields = ('actors', )

class ActorSerializer(serializers.ModelSerializer):

    class Movies(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', )
            read_only_fields = ('actors', )

    movies = Movies(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'movies', 'name', )

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content', )
        read_only_fields = ('movie', )

class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewListSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)

    class Actors(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name', )
        
    actors = Actors(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'actors', 'review_set', 'review_count', 'title', 'overview', 'release_date', 'poster_path', )

class ReviewSerializer(serializers.ModelSerializer):

    class Movie(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', )
            read_only_fields = ('actors', )
    
    movie = Movie(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'content', )
        read_only_fields = ('movie', )