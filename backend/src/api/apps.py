from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.api'

    def ready(self):
        import src.api.signals  # noqa: F401
