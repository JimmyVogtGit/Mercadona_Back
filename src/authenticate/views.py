import json
from django.contrib.auth import get_user_model,authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User



User = get_user_model()

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        email = data.get('email')
        name = data.get('name')
        password = data.get('password')

        if User.objects.filter(username=name).exists():
            return JsonResponse({'error': 'Username already exists'})
        if email and name and password:
            User.objects.create_user(username=name,email=email, password=password)
            return JsonResponse({'success': True, 'message' : 'Utilisateur ajouté avec succès !'})
        else:
            return JsonResponse({'success': False, 'message': 'Veuillez remplir tous les champs.'})
    else:
        return JsonResponse({'success': False, 'message': 'La requête doit être de type POST.'})


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('name')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'userName': username})
    return JsonResponse({'success': False})

def users_list(request):
    users = User.objects.all()
    usersList = []
    for user in users:
        usersList.append({
            'name': user.username,
            'email': user.email
        })
    return JsonResponse(usersList, safe=False)