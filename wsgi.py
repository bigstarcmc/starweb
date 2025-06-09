# starweb/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'starweb.settings')  # starweb으로 경로 설정

application = get_wsgi_application()
