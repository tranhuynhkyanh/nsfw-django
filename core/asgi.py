# mysite/asgi.py
import os

import django
from django.core.asgi import get_asgi_application

django.setup()


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Import modules that depend on Django's application registry

# Initialize Django ASGI application after setup
django_asgi_app = get_asgi_application()

application = django_asgi_app