import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'Schmetterling.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = os.path.abspath(__file__ + '/../..')

if path not in sys.path:
    sys.path.append(path)
