from django.test import SimpleTestCase
from django.urls import resolve, reverse
from .views import (
    category_list,
    create_category,
    create_product,
    product_list,
    create_promotion,
)

from django.test import TestCase, Client
from .models import Category
import json

from django.test import TestCase
from .models import Promotion, Produit, Category


class TestUrls(SimpleTestCase):
    def test_category_list_url_resolves(self):
        url = reverse('category_list')
        self.assertEqual(resolve(url).func, category_list)

    def test_create_category_url_resolves(self):
        url = reverse('create_category')
        self.assertEqual(resolve(url).func, create_category)

    def test_create_product_url_resolves(self):
        url = reverse('create_product')
        self.assertEqual(resolve(url).func, create_product)

    def test_product_list_url_resolves(self):
        url = reverse('products_list')
        self.assertEqual(resolve(url).func, product_list)

    def test_create_promotion_url_resolves(self):
        url = reverse('create_promotion')
        self.assertEqual(resolve(url).func, create_promotion)


class PromotionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuration des données de test
        category = Category.objects.create(id=2)
        produit = Produit.objects.create(wording='Produit de test', describe="test describe", price=1.2,
                                         image="img_url", category=category)
        Promotion.objects.create(percentage=20, produit=produit)

    def test_percentage_field(self):
        promotion = Promotion.objects.get(id=1)
        field_label = promotion._meta.get_field('percentage').verbose_name
        max_length = promotion._meta.get_field('percentage').max_length
        null = promotion._meta.get_field('percentage').null
        blank = promotion._meta.get_field('percentage').blank

        self.assertEqual(field_label, 'percentage')
        self.assertEqual(max_length, None)  # Supprimer cette assertion si vous définissez une limite de longueur
        self.assertEqual(null, False)
        self.assertEqual(blank, False)

    def test_startDate_field(self):
        promotion = Promotion.objects.get(id=1)
        field_label = promotion._meta.get_field('startDate').verbose_name
        null = promotion._meta.get_field('startDate').null
        blank = promotion._meta.get_field('startDate').blank

        self.assertEqual(field_label, 'startDate')
        self.assertEqual(null, True)
        self.assertEqual(blank, True)

    def test_endDate_field(self):
        promotion = Promotion.objects.get(id=1)
        field_label = promotion._meta.get_field('endDate').verbose_name
        null = promotion._meta.get_field('endDate').null
        blank = promotion._meta.get_field('endDate').blank

        self.assertEqual(field_label, 'endDate')
        self.assertEqual(null, True)
        self.assertEqual(blank, True)

    def test_produit_field(self):
        promotion = Promotion.objects.get(id=1)
        field_label = promotion._meta.get_field('produit').verbose_name
        related_model = promotion._meta.get_field('produit').related_model

        self.assertEqual(field_label, 'produit')
        self.assertEqual(related_model, Produit)


class PromotionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuration des données de test
        category = Category.objects.create(id=2)
        produit = Produit.objects.create(wording='Produit de test', describe="test describe", price=1.2,
                                         image="img_url", category=category)

        Promotion.objects.create(percentage=20, produit=produit)

    def test_percentage_field(self):
        promotion = Promotion.objects.get(id=1)
        field_label = promotion._meta.get_field('percentage').verbose_name
        null = promotion._meta.get_field('percentage').null
        blank = promotion._meta.get_field('percentage').blank

        self.assertEqual(field_label, 'percentage')
        self.assertEqual(null, False)
        self.assertEqual(blank, False)

    def test_startDate_field(self):
        promotion = Promotion.objects.get(id=1)
        field_label = promotion._meta.get_field('startDate').verbose_name
        null = promotion._meta.get_field('startDate').null
        blank = promotion._meta.get_field('startDate').blank

        self.assertEqual(field_label, 'startDate')
        self.assertEqual(null, True)
        self.assertEqual(blank, True)

    def test_endDate_field(self):
        promotion = Promotion.objects.get(id=1)
        field_label = promotion._meta.get_field('endDate').verbose_name
        null = promotion._meta.get_field('endDate').null
        blank = promotion._meta.get_field('endDate').blank

        self.assertEqual(field_label, 'endDate')
        self.assertEqual(null, True)
        self.assertEqual(blank, True)

    def test_produit_field(self):
        promotion = Promotion.objects.get(id=1)
        field_label = promotion._meta.get_field('produit').verbose_name
        related_model = promotion._meta.get_field('produit').related_model

        self.assertEqual(field_label, 'produit')
        self.assertEqual(related_model, Produit)


class CategoryListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuration des données de test
        Category.objects.create(name='Category 1')
        Category.objects.create(name='Category 2')

    def test_category_list_view(self):
        client = Client()
        response = client.get('/category-list/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

        # Convertir la réponse JSON en liste de dictionnaires
        category_list = json.loads(response.content.decode())

        # Vérifier le contenu de la réponse
        self.assertEqual(len(category_list), 2)

        category1 = category_list[0]
        self.assertEqual(category1['id'], 1)
        self.assertEqual(category1['name'], 'Category 1')

        category2 = category_list[1]
        self.assertEqual(category2['id'], 2)
        self.assertEqual(category2['name'], 'Category 2')
