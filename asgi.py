# starweb/asgi.py

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'starweb.settings')  # starweb으로 경로 설정

application = get_asgi_application()
