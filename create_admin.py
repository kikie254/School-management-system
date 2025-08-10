import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_sms.settings')
django.setup()
from django.contrib.auth.models import User
username = os.getenv('ADMIN_USERNAME', 'admin')
email = os.getenv('ADMIN_EMAIL', 'admin@schooldemo.ke')
password = os.getenv('ADMIN_PASSWORD', 'AdminPass2025')
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('Admin user created:', username)
else:
    print('Admin user already exists:', username)
