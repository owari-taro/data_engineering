from celery import Celery
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")

app=Celery("config",
           #task_routes = {'sample.tasks.save': {'queue': 'save'}   }
)
app.config_from_object("django.conf:settings",
                       namespace="CELERY")

app.autodiscover_tasks()