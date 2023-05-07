from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Produit, Promotion



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
        print(data)
        wording = data.get('wording')
        describe = data.get('describe')
        price = data.get('price')
        # image = data.get('image')
        category_id = data.get('category')
        promotion_id = data.get('promotion')
        category = Category.objects.get(pk=category_id)
        promotion = Promotion.objects.get(pk=promotion_id) if promotion_id else None

        produit = Produit(
            wording=wording,
            describe=describe,
            price=price,
            # image=image,
            category=category,
            promotion=promotion
        )

        produit.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


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
            'id':category.id,
            'name':category.name
        })
    return JsonResponse(category_list, safe=False)
