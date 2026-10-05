import os

from django.core.wsgi import get_wsgi_application

# Use render settings if DATABASE_URL is set (Render environment)
if 'DATABASE_URL' in os.environ:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wlg_backend.settings.render')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wlg_backend.settings.prod')

application = get_wsgi_application()
