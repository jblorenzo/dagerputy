from __future__ import absolute_import

import os
from datetime import timedelta

from django.conf import settings
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dagerputy.settings')

app = Celery('dagerputy')
app.config_from_object('dagerputy.celeryconfig')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-all-checks': {
        'task': 'dagerputy.dagerputyapp.tasks.run_all_checks',
        'schedule': timedelta(seconds=60),
    },
    'update-shifts': {
        'task': 'dagerputy.dagerputyapp.tasks.update_shifts',
        'schedule': timedelta(seconds=1800),
    },
    'clean-db': {
        'task': 'dagerputy.dagerputyapp.tasks.clean_db',
        'schedule': timedelta(seconds=60 * 60 * 24),
    },
}
