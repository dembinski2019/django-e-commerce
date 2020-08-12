from django.test import TestCase,Client
from django.conf import settings
from model_mommy import mommy
from checkout.models import CartItem, Order
from django.urls import reverse


class CartItemTestCase(TestCase):

    def setUp(self):
        mommy.make(CartItem, _quantity=3)

    def test_post_save_cart_item(self):
        cart_item = CartItem.objects.all()[0]
        cart_item.quantity = 0
        cart_item.save()
        self.assertEquals(CartItem.objects.count(),2)


class OrderTestCase(TestCase):

    def setUp(self):
        self.cart_item = mommy.make(CartItem)
        self.user = mommy.make(settings.AUTH_USER_MODEL)


    def test_create_order(self):
        Order.objects.create_order(self.user, [self.cart_item])
        self.assertEquals(Order.objects.count(),1)
        order = Order.objects.get()
        self.assertEquals(order.user, self.user)
        order_item = order.items.get()
        self.assertEquals(order_item.product, self.cart_item.product)

class CheckoutViewTestCase(TestCase):

    def setUp(self):
        self.user = mommy.make(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()
        self.cart_item = mommy.make(CartItem)
        self.client = Client()
        self.checkout_url=reverse('checkout:checkout_view')


    def test_checkout_view(self):
        response= self.client.get(self.checkout_url)
        redirect_url = f'{reverse(settings.LOGIN_URL)}?next={self.checkout_url}'
        self.assertRedirects(response,redirect_url)
        self.client.login(username=self.user.username, password='123')
        self.cart_item.cart_key = self.client.session.session_key
        self.cart_item.save()
        response=self.client.get(self.checkout_url)
        self.assertTemplateUsed(response,'checkout/checkout.html')
