import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.conf import settings
from django.core.asgi import get_asgi_application

from backend.api.v1 import routing as chat_routing
from backend.api.v1.middleware import JWTAuthMiddlewareStack

settings_module = os.getenv(
    "DJANGO_SETTINGS_MODULE",
    "backend.config.settings.dev",
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            JWTAuthMiddlewareStack(
                URLRouter(chat_routing.websocket_urlpatterns),
            ),
        ),
    },
)


if settings.DEBUG:
    from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler

    application = ProtocolTypeRouter(
        {
            "http": ASGIStaticFilesHandler(django_asgi_app),
            "websocket": AllowedHostsOriginValidator(
                JWTAuthMiddlewareStack(
                    URLRouter(chat_routing.websocket_urlpatterns),
                ),
            ),
        },
    )
