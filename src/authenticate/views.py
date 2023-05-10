import json
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes

from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import IsAuthenticated


class LoginView(TokenObtainPairView):
    pass


User = get_user_model()

'''def login_user(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            username = data.get('name')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True, 'userName': username})
        return JsonResponse({'success': False})'''


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
            User.objects.create_user(username=name, email=email, password=password)
            return JsonResponse({'success': True, 'message': 'Utilisateur ajouté avec succès !'})
        else:
            return JsonResponse({'success': False, 'message': 'Veuillez remplir tous les champs.'})
    else:
        return JsonResponse({'success': False, 'message': 'La requête doit être de type POST.'})


'''@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('name')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'userName': username})
    return JsonResponse({'success': False})'''

'''class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return self.userList(request, *args, **kwargs)
        return self.http_method_not_allowed(request, *args, **kwargs)

    def userList(self, request):
        users = User.objects.all()
        usersList = []
        for user in users:
            usersList.append({
                'name': user.username,
                'email': user.email
            })
        return JsonResponse(usersList, safe=False)'''


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):
    users = User.objects.all()
    usersList = []
    for user in users:
        usersList.append({
            'name': user.username,
            'email': user.email
        })
    return JsonResponse(usersList, safe=False)
