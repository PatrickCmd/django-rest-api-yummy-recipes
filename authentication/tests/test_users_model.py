from django.test import TestCase
from django.utils import timezone

from authentication.models import User


class UserModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            first_name="test",
            last_name="user",
            username='test1',
            email='test1@test.com',
            password='test12345'
        )
    
    def test_user_creation(self):
        user = User.objects.create_user(
            username='test12',
            email='test12@test.com',
            password='test12345'
        )
        now = timezone.now()
        self.assertEqual(user.username, 'test12')
        self.assertLess(user.created_at, now)
    
    def test_get_user_string_rep(self):
        self.assertEqual(str(self.user), self.user.username)
    
    def test_get_user_short_name(self):
        self.assertEqual(self.user.get_short_name(), 'test')
    
    def test_get_user_full_name(self):
        self.assertEqual(self.user.get_full_name(), 'test user')
    
    # def test_user_creation_no_username(self):
    #     with self.assertRaises(TypeError, 'Users must have a username'):
    #         User.objects.create_user(
    #             None,
    #             email='test12@test.com',
    #             password='test12345'
    #         )
    
    def test_super_user_creation(self):
        user = User.objects.create_superuser(
            username='test123',
            email='test123@test.com',
            password='test12345'
        )
        now = timezone.now()
        self.assertEqual(user.username, 'test123')
        self.assertEqual(user.is_superuser, True)
        self.assertEqual(user.is_staff, True)
        self.assertLess(user.created_at, now)
