from django.test import TestCase
from .models import Item, Category

class TestItemListView(TestCase):

    def test_response_status_code(self):
        response = self.client.get('/items/')
        self.assertEqual(response.status_code, 200)
        print('check status 200')


    def test_response_context(self):
        response = self.client.get('/items/')
        self.assertIn('help_text', response.context)
        self.assertEqual(response.context['help_text'], 'Click on Item to get more information')
        print('check context')


class TestItemDetailView(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name='Vegetables')
        self.item = Item.objects.create(name='Potatoes', desc='blablablabla', category=self.category)

    def tearDown(self) -> None:
        self.item.delete()
        self.category.delete()

    def test_item_detail_negative(self):
        response = self.client.get('/items/999/')
        self.assertEqual(response.status_code, 404)
        print('check item detail negative')

    def test_item_detail(self):
        response = self.client.get(f'/items/{self.item.pk}/')
        self.assertEqual(response.status_code, 200)
        print('check item detail positive')

    def test_response_status_code(self):
        response = self.client.get('/items/')
        self.assertEqual(response.status_code, 200)
        print('check status 200')