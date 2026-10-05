import os
import sys

# Set Django settings - render.py is production-ready and doesn't need decouple
if 'DATABASE_URL' in os.environ or 'render' in os.environ.get('HOME', ''):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'wlg_backend.settings.render'
else:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'wlg_backend.settings.dev'

from django.core.wsgi import get_wsgi_application

try:
    application = get_wsgi_application()
except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr)
    raise
