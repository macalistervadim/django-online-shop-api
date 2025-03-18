from django.urls import re_path

from backend.api.v1.consumers import AdminChatConsumer, UserChatConsumer

websocket_urlpatterns = [
    re_path(r"ws/admin/", AdminChatConsumer.as_asgi()),
    re_path(
        r"ws/chat/room/(?P<chat_id>\d+)/$",
        UserChatConsumer.as_asgi(),
    ),
]
