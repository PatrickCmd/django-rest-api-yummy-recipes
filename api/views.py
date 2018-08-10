from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)

from .models import (
    Category, Recipe, Review, Upvote
)
from .serializers import (
    CategorySerializer, RecipeSerializer,
    ReviewSerialiZer, UpvoteSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    
    def get_queryset(self):
        # list  categories per current loggedin user
        queryset = Category.objects.all().filter(owner=self.request.user)
        return queryset
    serializer_class = CategorySerializer

    def create(self, request):
        # check if category already exists for current logged in user
        category = Category.objects.filter(
            name=request.data.get('name'),
            owner=request.user
        )
        if category:
            msg='Category with that name already exists'
            raise ValidationError(msg)
        return super().create(request)
    
    # user can only delete category he created
    def destroy(self, request, *args, **kwargs):
        category = Category.objects.get(pk=self.kwargs["pk"])
        if not request.user == category.owner:
            raise PermissionDenied("You can not delete this category")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryRecipes(generics.ListCreateAPIView):
    
    def get_queryset(self):
        if self.kwargs.get("category_pk"):
            category = Category.objects.get(pk=self.kwargs["category_pk"])
            queryset = Recipe.objects.filter(
                owner=self.request.user,
                category=category
            )
        return queryset
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SingleCategoryRecipe(generics.RetrieveUpdateDestroyAPIView):
    
    def get_queryset(self):
        if self.kwargs.get("category_pk") and self.kwargs.get("pk"):
            category = Category.objects.get(pk=self.kwargs["category_pk"])
            queryset = Recipe.objects.filter(
                pk=self.kwargs["pk"],
                owner=self.request.user,
                category=category
            )
        return queryset
    serializer_class = RecipeSerializer


class RecipesViewSet(viewsets.ModelViewSet):
    
    def get_queryset(self):
        queryset = Recipe.objects.all().filter(owner=self.request.user)
        return queryset
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
