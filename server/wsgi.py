import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()

# Add this for Vercel deployment
app = application  # Vercel looks for 'app' or 'handler'