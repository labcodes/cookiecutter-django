import os
import environ
from celery import Celery


env = environ.Env()

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
# https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-APPLICATION-NAME
# NOTE: application name must be an ASCII string
# with only printable characters and a maximum
# of 64 characters in length
application_name = env.str(
    "DJANGO_DATABASE_APPLICATION_NAME",
    default="{{cookiecutter.project_slug}}_celery"
)
application_name = application_name[:64]
os.environ["DJANGO_DATABASE_APPLICATION_NAME"] = application_name

app = Celery("{{cookiecutter.project_slug}}")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
