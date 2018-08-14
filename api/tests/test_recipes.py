from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from api import views
from api.models import Category, Recipe, Review


class TestRecipesTestCase(APITestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.recipes_view = views.RecipesViewSet.as_view({'get': 'list',
                                                         'post': 'create'})
        self.single_recipe_view = views.RecipesViewSet.as_view(
            {'get': 'retrieve', 'delete': 'destroy'}
        )
        self.category_recipes_view = views.CategoryRecipes.as_view()
        self.public_recipes_view = views.PublicRecipes.as_view()
        self.public_recipes_detail = views.PublicRecipesDetail.as_view()
        self.recipe_reviews = views.RecipeReviews.as_view({'get': 'list', 
                                                          'post': 'create'})
        self.category_uri = '/categories/'
        self.recipe_uri = '/recipes/'
        self.public_recipes_uri = '/public-recipes/'
        self.test_user = self.setup_user()
        self.category = self.setup_category()
        self.recipe = self.setup_recipe()
        self.public_recipe = self.setup_public_recipe()
        self.recipe_review = self.setup_recipe_review()
    
    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            username='test1',
            email='test1@test.com',
            password='test12345'
        )
    
    @staticmethod
    def setup_category():
        category = Category.objects.create(
            name='test category',
            owner=get_user_model().objects.get(username='test1'),
            description='sweet and flavor category'
        )
        category.save()
        return category
    
    @staticmethod
    def setup_recipe():
        recipe = Recipe.objects.create(
            name='test recipe',
            owner=get_user_model().objects.get(username='test1'),
            category=Category.objects.get(name='test category'),
            description='sweet and flavor recipe',
            ingredients = 'Onions, Tomatoes'
        )
        recipe.save()
        return recipe
    
    @staticmethod
    def setup_public_recipe():
        recipe = Recipe.objects.create(
            name='test public recipe',
            owner=get_user_model().objects.get(username='test1'),
            category=Category.objects.get(name='test category'),
            description='sweet and flavor recipe',
            ingredients='Onions, Tomatoes',
            is_public=True
        )
        recipe.save()
        return recipe
    
    @staticmethod
    def setup_recipe_review():
        review = Review.objects.create(
            comment="Awesome recipe",
            recipe=Recipe.objects.get(name='test public recipe')
        )
        review.save()
        return review
    
    def test_recipes_list(self):
        '''
        test retrieve all user recipes
        '''
        request = self.factory.get(self.recipe_uri)
        force_authenticate(request, user=self.test_user)
        response = self.recipes_view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('test recipe', str(response.data))
    
    def test_get_single_recipes(self):
        '''
        test retrieve a single user recipe
        '''
        request = self.factory.get(self.recipe_uri)
        force_authenticate(request, user=self.test_user)
        pk = Recipe.objects.get(name='test recipe').pk
        response = self.single_recipe_view(request, pk=pk)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('test recipe', str(response.data))
    
    def test_get_single_recipes_not_found(self):
        '''
        test retrieve a single user recipe not found
        '''
        request = self.factory.get(self.category_uri)
        force_authenticate(request, user=self.test_user)
        response = self.single_recipe_view(request, pk=8)
        self.assertEqual(response.status_code, 404,
                         'Expected Response Code 404, received {0} instead.'
                         .format(response.status_code))
        self.assertNotIn('test recipe', str(response.data))
    
    def test_category_recipes_list(self):
        '''
        test retrieve all user recipes in category
        '''
        request = self.factory.get(self.category_uri)
        force_authenticate(request, user=self.test_user)
        category_pk = Category.objects.get(name='test category').pk
        response = self.category_recipes_view(request, category_pk=category_pk)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('test recipe', str(response.data))
    
    def test_single_category_recipe(self):
        '''
        test retrieve a single recipe in category
        '''
        request = self.factory.get(self.category_uri)
        force_authenticate(request, user=self.test_user)
        pk = Recipe.objects.get(name='test recipe').pk
        category_pk = Category.objects.get(name='test category').pk
        response = self.single_recipe_view(request, category_pk=category_pk,
                                           pk=pk)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('test recipe', str(response.data))
    
    def test_create_recipe(self):
        '''
        test create user recipes
        '''
        params = {
            'name': 'test recipe2',
            'category': Category.objects.get(name='test category').pk,
            'description': 'sweet and flavor recipe',
            'ingredients': 'Onions, Tomatoes'
        }
        request = self.factory.post(self.recipe_uri, params, format='json')
        force_authenticate(request, user=self.test_user)
        response = self.recipes_view(request)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('test recipe2', str(response.data))
    
    def test_create_category_recipe(self):
        '''
        test create user category recipes
        '''
        params = {
            'name': 'test recipe3',
            'category': Category.objects.get(name='test category').pk,
            'description': 'sweet and flavor recipe',
            'ingredients': 'Onions, Tomatoes'
        }
        request = self.factory.post(self.category_uri, params, format='json')
        force_authenticate(request, user=self.test_user)
        category_pk = Category.objects.get(name='test category').pk
        response = self.category_recipes_view(request, category_pk=category_pk)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('test recipe3', str(response.data))
    
    def test_public_recipes_list(self):
        '''
        test retrieve all public recipes
        '''
        request = self.factory.get(self.public_recipes_uri)
        response = self.public_recipes_view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('test public recipe', str(response.data))
    
    def test_get_public_recipe_detail(self):
        '''
        test retrieve a single public recipe
        '''
        request = self.factory.get(self.public_recipes_uri)
        pk = Recipe.objects.filter(is_public=True).first().pk
        response = self.public_recipes_detail(request, pk=pk)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('test public recipe', str(response.data))
    
    def test_get_recipe_reviews(self):
        '''
        test retrieve recipe reviews
        '''
        request = self.factory.get(self.public_recipes_uri)
        pk = Recipe.objects.filter(is_public=True).first().pk
        response = self.recipe_reviews(request, pk=pk)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('Awesome recipe', str(response.data))
