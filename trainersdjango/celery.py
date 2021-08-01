import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trainersdjango.settings")

app = Celery("trainersdjango")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.timezone = 'Europe/Warsaw'

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')