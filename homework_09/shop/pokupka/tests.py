from django.test import TestCase
from .models import Category, Item, User, Cart

class TestCategory(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name='Vegetables')

    def tearDown(self) -> None:
        self.category.delete()

    def test_init(self):
        self.assertTrue(isinstance(self.category.name, str))
        self.assertEqual(self.category.name, 'Vegetables')

class TestItem(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name='Vegetables')
        self.item = Item.objects.create(name='Potatoes', desc='blablablabla', category=self.category)

    def tearDown(self) -> None:
        self.item.delete()
        self.category.delete()


    def test_name(self):
        self.assertTrue(isinstance(self.item.name, str))
        self.assertEqual(self.item.name, 'Potatoes')

    def test_desc(self):
        self.assertTrue(isinstance(self.item.desc, str))
        self.assertEqual(self.item.desc, 'blablablabla')


class TestUser(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(first_name='Praskovia', last_name='Nezhdanova')

    def tearDown(self) -> None:
        self.user.delete()

    def test_first_name(self):
        self.assertTrue(isinstance(self.user.first_name, str))
        self.assertEqual(self.user.first_name, 'Praskovia')

    def test_last_name(self):
        self.assertTrue(isinstance(self.user.last_name, str))
        self.assertEqual(self.user.last_name, 'Nezhdanova')
