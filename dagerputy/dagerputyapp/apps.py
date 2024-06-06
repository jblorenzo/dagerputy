from django.apps import AppConfig
from django.db.models.signals import post_migrate


def post_migrate_callback(**kwargs):
    from dagerputy.dagerputyapp.alert import update_alert_plugins
    from dagerputy.dagerputyapp.models import create_default_jenkins_config
    update_alert_plugins()
    create_default_jenkins_config()

class DagerputyappConfig(AppConfig):
    name = 'dagerputy.dagerputyapp'

    def ready(self):
        post_migrate.connect(post_migrate_callback, sender=self)
