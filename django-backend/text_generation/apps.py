from django.apps import AppConfig


class TextGenerationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'text_generation'

    def ready(self):
        import os
        if os.environ.get('RUN_MAIN') == 'true':
            from .predictors.model_store import model_store
            model_store.initialize()
