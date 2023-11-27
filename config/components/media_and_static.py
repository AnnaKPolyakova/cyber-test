import os

from django.conf import settings

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(settings.BASE_DIR, "media")
#
#
# if settings.DEBUG is False:
#     STATIC_ROOT = os.path.join(settings.BASE_DIR, "static")
# else:
#     STATICFILES_DIRS = (os.path.join(settings.BASE_DIR, "static/"),)

STATIC_ROOT = os.path.join(settings.BASE_DIR, "static")

