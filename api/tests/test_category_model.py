from django.test import TestCase

from api.models import Category


class TestCategoryModel(TestCase):

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
