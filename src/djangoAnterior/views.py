import os

from django.http import HttpResponse


def index(request):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    public_html_dir = os.path.abspath(os.path.join(current_dir, '../../../public_html'))
    index_html = os.path.join(public_html_dir, 'index.html')

    # Lire le contenu du fichier index.html
    with open(index_html, 'r') as file:
        content = file.read()

    return HttpResponse(content)
