from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from api import views
from api.models import Category


class TestCategoryTestCase(APITestCase):
    
    def setUp(self):
        
        self.factory = APIRequestFactory()
        self.view = views.CategoryViewSet.as_view({'get': 'list',
                                                  'post': 'create'})
        self.view_detail = views.CategoryViewSet.as_view({'get': 'retrieve',
                                                          'delete': 'destroy'})
        self.uri = '/api/categories/'
        self.test_user = self.setup_user()
        self.category = self.setup_category()
    
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
    
    def test_create_category(self):
        '''
        test create category
        '''
        params = {
            'name': 'test2 category',
            'description': 'sweet and flavor category'
        }
        request = self.factory.post(self.uri, params)
        force_authenticate(request, user=self.test_user)
        response = self.view(request)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('test2 category', str(response.data))
    
    def test_create_already_existing_category(self):
        '''
        test create category already existing
        '''
        params = {
            'name': 'test category',
            'description': 'sweet and flavor category'
        }
        request = self.factory.post(self.uri, params)
        force_authenticate(request, user=self.test_user)
        response = self.view(request)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('Category with that name already exists',
                      str(response.data))

    def test_category_list(self):
        '''
        test retrieve all categories
        '''
        request = self.factory.get(self.uri)
        force_authenticate(request, user=self.test_user)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('test category', str(response.data))
    
    def test_category_detail(self):
        '''
        test retrieve category detail
        '''
        request = self.factory.get(self.uri)
        force_authenticate(request, user=self.test_user)
        response = self.view_detail(request, pk=1)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('test category', str(response.data))
    
    def test_category_detail_destroy(self):
        '''
        test delete category detail
        '''
        request = self.factory.delete(self.uri)
        force_authenticate(request, user=self.test_user)
        response = self.view_detail(request, pk=1)
        self.assertEqual(response.status_code, 204,
                         'Expected Response Code 204, received {0} instead.'
                         .format(response.status_code))
        self.assertNotIn('test category', str(response.data))
    
    def test_category_not_existing_detail(self):
        '''
        test retrieve category detail when not existing
        '''
        request = self.factory.get(self.uri)
        force_authenticate(request, user=self.test_user)
        response = self.view_detail(request, pk=2)
        self.assertEqual(response.status_code, 404,
                         'Expected Response Code 404, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('Not found', str(response.data))
