from django.test import TestCase
from django.contrib.auth.models import User
from product.models.product import Product
from order.models.order import Order
from order.serializers.order_serializer import OrderSerializer


class OrderSerializerTest(TestCase):
    def test_serialization_with_products(self):
        user = User.objects.create(username="henrique")

        product1 = Product.objects.create(
            title="Livro A",
            description="Descrição A",
            price=30,
            active=True
        )
        product2 = Product.objects.create(
            title="Livro B",
            description="Descrição B",
            price=20,
            active=True
        )

        order = Order.objects.create(user=user)
        order.product.add(product1, product2)

        serializer = OrderSerializer(order)
        data = serializer.data

        self.assertEqual(len(data['product']), 2)
        self.assertEqual(data['total'], 50)
