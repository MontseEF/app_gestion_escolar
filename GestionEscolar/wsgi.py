"""
WSGI config for GestionEscolar project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import sys
import os

# Ruta a tu proyecto
project_path = '/home/montserratespinozaflores/app_gestion_escolar'
if project_path not in sys.path:
    sys.path.append(project_path)

# Activar entorno virtual
activate_this = '/home/montserratespinozaflores/app_gestion_escolar/.venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestionEscolar.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()