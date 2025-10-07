from django.test import TestCase
from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer


class ProductSerializerTest(TestCase):
    def test_serialization(self):
        product = Product.objects.create(
            title="Livro Teste",
            description="Descrição livro teste",
            price=25,
            active=True
        )

        serializer = ProductSerializer(product)
        data = serializer.data

        self.assertEqual(data['title'], "Livro Teste")
        self.assertEqual(data['description'], "Descrição livro teste")
        self.assertEqual(int(data['price']), 25)
        self.assertEqual(bool(data['active']), True)
