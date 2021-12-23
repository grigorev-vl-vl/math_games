from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# The directory where collectstatic will copy static files
STATIC_ROOT = os.path.join(BASE_DIR, 'static')