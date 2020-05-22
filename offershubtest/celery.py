from __future__ import absolute_import, unicode_literals

import logging
import os

from celery import Celery
from sentry_sdk.integrations.logging import LoggingIntegration

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'offershubtest.settings')

app = Celery('offershubtest')



app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

import sentry_sdk
from sentry_sdk.integrations.celery import \
    CeleryIntegration
sentry_logging = LoggingIntegration(
    level=logging.INFO,        # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)
sentry_sdk.init(
    dsn="https://4294813e4ecd4990a7cad9167302e52c@o134471.ingest.sentry.io/5245208",
    integrations=[CeleryIntegration(), sentry_logging]
)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
