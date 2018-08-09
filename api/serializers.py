from rest_framework import serializers

from .models import (
    Category, Recipe, Review, Upvote
)


class ReviewSerialiZer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class UpvoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upvote
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    reviews = ReviewSerialiZer(many=True, read_only=True, required=False)
    upvotes = UpvoteSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Recipe
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    recipes = RecipeSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'owner', 'description', 'recipes',
                  'created_at', 'updated_at')