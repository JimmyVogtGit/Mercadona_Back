"""
WSGI config for djangoAnterior project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/jimbigood/Documents/projects/studi/Django/django_with_postgresql_9622/Back/src')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoAnterior.settings')

application = get_wsgi_application()
