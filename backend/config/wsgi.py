import os

from django.core.wsgi import get_wsgi_application

settings_module = os.getenv(
    "DJANGO_SETTINGS_MODULE",
    "backend.config.settings.dev",
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
