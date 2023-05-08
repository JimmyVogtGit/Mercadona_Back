# Create your views here.
import json
from datetime import datetime

import pytz
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Category, Produit, Promotion

tz = pytz.timezone('Europe/Paris')

"""class ProduitViewSet(viewsets.ModelVieSet):
    queryset = Produit.objects.all()
    serializer_class= ProduitSerializer

    @csrf_exempt
    def create_product(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = json.loads(request.body.decode("utf-8"))
            print(data)
            wording = data.get('wording')
            describe = data.get('describe')
            price = data.get('price')
            image = data.get('image')
            category_id = data.get('category')
            promotion_id = data.get('promotion')

            category = Category.objects.get(pk=category_id)
            promotion = Promotion.objects.get(pk=promotion_id) if promotion_id else None

            Produit.objects.create(
                wording=wording,
                describe=describe,
                price=price,
                image=image,
                category=category,
                promotion=promotion
            )

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'})"""


@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        wording = data.get('wording')
        describe = data.get('describe')
        price = data.get('price')
        # image = data.get('image')
        category_id = data.get('category')
        promotion_id = data.get('promotion')
        category = Category.objects.get(pk=category_id)

        produit = Produit(
            wording=wording,
            describe=describe,
            price=price,
            # image=image,
            category=category,

        )

        produit.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def product_list(request):
    products = Produit.objects.prefetch_related('promotion_set', 'category')
    products_list = []

    for product in products:
        promotions = []
        for promotion in product.promotion_set.all():
            promotions.append({
                'id': promotion.id,
                'percentage': promotion.percentage
            })
        products_list.append({
            'id': product.id,
            'wording': product.wording,
            "describe": product.describe,
            "price": product.price,
            "category": product.category.name,
            "image": product.image if product.image else None,
            "promotion": promotions

        })
    return JsonResponse(products_list, safe=False)


@csrf_exempt
def create_category(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        wording = data.get('wording')
        category = Category(wording=wording)
        category.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def category_list(request):
    categories = Category.objects.all()
    category_list = []
    for category in categories:
        category_list.append({
            'id': category.id,
            'name': category.name
        })
    return JsonResponse(category_list, safe=False)


@csrf_exempt
def create_promotion(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        percent = data.get("percent")
        start_date = tz.localize(datetime.strptime(data.get("startDate"), '%Y-%m-%d'))
        end_date = tz.localize(datetime.strptime(data.get("endDate"), '%Y-%m-%d'))
        product_id = data.get("productId")

    existing_product = Produit.objects.get(id=product_id)
    existing_promotion = Promotion.objects.filter(produit=product_id).first()

    if existing_promotion is not None:
        existing_promotion.percentage = percent
        existing_promotion.startDate = start_date
        existing_promotion.endDate = end_date
        existing_promotion.save()
        return JsonResponse({"status": "success", "message": "Modified promotion with success"})

    else:
        promotion = Promotion(percentage=percent, startDate=start_date, endDate=end_date, produit=existing_product)
        promotion.save()
        return JsonResponse({"status": "success", "message": "Creating promotion with success"})
