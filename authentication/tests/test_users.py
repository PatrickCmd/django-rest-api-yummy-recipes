from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from authentication import views


class TestUserTestCase(APITestCase):
    
    def setUp(self):
        
        self.factory = APIRequestFactory()
        self.register_view = views.RegistrationAPIView.as_view()
        self.login_view = views.LoginAPIView.as_view()
        self.list_users_view = views.UserListViewSet.as_view({'get': 'list'})
        self.uri = '/users/register'
        self.users_list_uri = '/users'
        self.login_uri = '/users/login'
        self.test_user = self.setup_user()
    
    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            username='test1',
            email='test1@test.com',
            password='test12345'
        )
    
    def test_register_user(self):
        '''
        test user registration
        '''
        params = {
            'username': 'test',
            'email': 'testuser@test.com',
            'password': 'test1234'
        }
        request = self.factory.post(self.uri, params, format='json')
        response = self.register_view(request)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))
    
    def test_get_users_list(self):
        '''
        test retrieve all users
        '''
        request = self.factory.get(self.users_list_uri)
        response = self.list_users_view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('test1', str(response.data))
    
    def test_user_login(self):
        '''
        test successful user login
        '''
        params = {
            'username': 'test1',
            'password': 'test12345'
        }
        request = self.factory.post(self.login_uri, params, format='json')
        response = self.login_view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertIn('token', str(response.data))
