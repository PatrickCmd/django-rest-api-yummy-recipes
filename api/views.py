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

    # Only authenticated users can create recipes
    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users with accounts can create recipes")
        return super().create(request, *args, **kwargs)
    
    # user can only delete recipe he created
    def destroy(self, request, *args, **kwargs):
        recipe  = Recipe.objects.get(pk=self.kwargs["pk"])
        if not request.user == recipe.owner:
            raise PermissionDenied(
                "You have no permissions to delete this recipe")
        return super().destroy(request, *args, **kwargs)
    
    # user can only delete category he created
    def update(self, request, *args, **kwargs):
        recipe  = Recipe.objects.get(pk=self.kwargs["pk"])
        if not request.user == recipe.owner:
            raise PermissionDenied(
                "You have no permissions to edit this recipe")
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PublicRecipes(generics.ListAPIView):
    
    permission_classes = ()
    
    def get_queryset(self):
        queryset = Recipe.objects.all().filter(is_public=True)
        return queryset
    serializer_class = RecipeSerializer


class PublicRecipesDetail(generics.RetrieveAPIView):
    permission_classes = ()
    
    def get_queryset(self):
        queryset = Recipe.objects.all().filter(is_public=True)
        return queryset
    serializer_class = RecipeSerializer
    

class RecipeReviews(viewsets.ModelViewSet):
    
    permission_classes = ()
    serializer_class = ReviewSerialiZer
    
    def get_queryset(self):
        queryset = Review.objects.all().filter(recipe=self.kwargs['pk'])
        return queryset


class UpVoteViewSet(viewsets.ModelViewSet):
    
    serializer_class = UpvoteSerializer

    def get_queryset(self):
        queryset = Upvote.objects.all().filter(recipe=self.kwargs['pk'])
        return queryset
    
    # A user can only upvote a recipe once
    def create(self, request, *args, **kwargs):
        upvote = Upvote.objects.filter(recipe=self.kwargs['pk']).first()
        if upvote and request.user == upvote.voted_by:
            raise PermissionDenied(
                "You can not vote for recipe more than once")
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(voted_by=self.request.user)
