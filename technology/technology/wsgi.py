"""
WSGI config for technology project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from selectenv import Selectenv

from django.core.wsgi import get_wsgi_application

env = Selectenv()
env.getenvironment()


application = get_wsgi_application()
