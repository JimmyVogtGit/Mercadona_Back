from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

@csrf_exempt
def create_user(request):
    if request.method == 'POST':

        email = request.headers.get('Email', None)
        name = request.headers.get('Name', None)
        password = request.headers.get('Password', None)

        if email and name and password:

            user = User.objects.create_user(username=name,email=email, password=password)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Veuillez remplir tous les champs.'})
    else:
        return JsonResponse({'success': False, 'message': 'La requête doit être de type POST.'})