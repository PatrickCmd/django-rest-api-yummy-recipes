from rest_framework import serializers

from .models import (
    Category, Recipe, Review, Upvote
)


class ReviewSerialiZer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class UpvoteSerializer(serializers.ModelSerializer):
    voted_by = serializers.ReadOnlyField(source='voted_by.username')
    class Meta:
        model = Upvote
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    reviews = ReviewSerialiZer(many=True, read_only=True, required=False)
    upvotes = UpvoteSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'description', 'owner', 'category',
                  'ingredients', 'reviews', 'upvotes', 'is_public',
                  'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    recipes = RecipeSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'owner', 'description', 'recipes',
                  'created_at', 'updated_at')
