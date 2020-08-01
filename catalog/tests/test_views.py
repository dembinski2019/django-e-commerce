from django.test import TestCase, Client
from model_mommy import mommy
from catalog.models import Category, Product
from django.urls import reverse


class ProductListTestCase(TestCase):

    def setUp(self):
        self.url = reverse('catalog:product_list')
        self.client = Client()
        self.products = mommy.make('catalog.Product',_quantity=10)

    def tearDown(self):
        Product.objects.all().delete()
        
    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/product_list.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('product_list' in response.context)
        product = response.context['product_list']
        self.assertEquals(product.count(), 3)
        paginator = response.context['paginator']
        self.assertEquals(paginator.num_pages,4)


    def test_page_not_found(self):
        response = self.client.get(f'{self.url}?page=5')
        self.assertEquals(response.status_code, 404)



