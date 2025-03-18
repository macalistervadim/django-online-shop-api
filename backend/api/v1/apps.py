from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.api.v1"
    verbose_name = "Api"

    def ready(self) -> None:
        import backend.api.v1.signals  # noqa: F401
