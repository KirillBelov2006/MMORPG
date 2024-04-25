import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MMORPG.settings')

app = Celery('MMORPG')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'Europe/Moscow'
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'send_mail_friday_12am': {
        'task': 'board.tasks.send_mail_friday_12am',
        'schedule': crontab(hour=12, minute=0, day_of_week='friday'),
    },
}
