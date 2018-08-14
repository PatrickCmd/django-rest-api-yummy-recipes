from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet, CategoryRecipes,
    SingleCategoryRecipe, RecipesViewSet, PublicRecipes,
    PublicRecipesDetail, RecipeReviews, UpVoteViewSet
)

router = DefaultRouter()
router.register('categories', CategoryViewSet, base_name='categories')
router.register('recipes', RecipesViewSet, base_name='recipes')

custom_urlpatterns = [
    url(r'categories/(?P<category_pk>\d+)/recipes$',
        CategoryRecipes.as_view(), name='category_recipes'),
    url(r'categories/(?P<category_pk>\d+)/recipes/(?P<pk>\d+)$',
        SingleCategoryRecipe.as_view(), name='single_category_recipe'),
    url(r'public-recipes/$', PublicRecipes.as_view(), name='public_recipes'),
    url(r'public-recipes/(?P<pk>\d+)/$', PublicRecipesDetail.as_view(),
        name='public_recipes_detail'),
    url(r'public-recipes/(?P<pk>\d+)/reviews/$',
        RecipeReviews.as_view({'get': 'list', 'post': 'create'}),
        name='recipe_reviews'),
    url(r'public-recipes/(?P<pk>\d+)/upvotes/$',
        UpVoteViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='recipe_upvotes'),
]

urlpatterns = router.urls

urlpatterns += custom_urlpatterns
