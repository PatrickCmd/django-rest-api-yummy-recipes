from django.test import TestCase

from api.models import Category
from authentication.models import User


class TestCategoryModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            first_name="test",
            last_name="user",
            username='test1',
            email='test1@test.com',
            password='test12345'
        )

        self.category = Category.objects.create(
            name='test category',
            owner=self.user,
            description='sweet and flavor category'
        )
    
    def test_category_name(self):
        self.assertEqual(self.category.name, 'test category')

    def test_string_representation(self):
        '''
        test category string representation
        '''
        category = Category(
            name="test category"
        )
        self.assertEqual(str(category), category.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Category._meta.verbose_name_plural),
                         "categories")
