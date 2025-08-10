from django.apps import AppConfig
import os

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        # Create admin user from env vars if not exists
        try:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            username = os.getenv('ADMIN_USERNAME')
            email = os.getenv('ADMIN_EMAIL')
            password = os.getenv('ADMIN_PASSWORD')
            if username and password and not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username, email or '', password)
        except Exception:
            # Avoid errors during manage.py commands before migrations
            pass
