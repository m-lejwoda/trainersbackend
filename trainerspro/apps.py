from django.apps import AppConfig


class TrainersproConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trainerspro'
    def ready(self):
        import trainerspro.signals
