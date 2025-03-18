from datetime import timedelta
from typing import Any

from django.core.management.base import BaseCommand
from django.utils.timezone import now

from backend.api.v1.models import Chat


class Command(BaseCommand):
    help = "Удаляет старые чаты и связанные сообщения"

    def handle(self, *args: tuple[Any], **kwargs: dict[Any, Any]) -> Any:
        one_year_ago = now() - timedelta(days=365)
        old_chats = Chat.objects.filter(created_at__lt=one_year_ago)

        count = old_chats.count()
        old_chats.delete()

        self.stdout.write(self.style.SUCCESS(f"Удалено {count} старых чатов"))
