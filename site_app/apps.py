from django.apps import AppConfig


class DjangoAppConfig(AppConfig):
    default_auto_field = 'site.db.models.BigAutoField'
    name = 'site_app'
