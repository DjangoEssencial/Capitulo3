import sys
import os

from django.conf import settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


settings.configure(
    DEBUG=True,
    SECRET_KEY='daiq1iuw1x^9bj4d8zx*+a0#*dh7ek86)zd^x61oesa17b_ny^',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
        #'django.contrib.webdesign', obsoleto a partir do django 1.8
    ),

    STATIC_URL='/static/',
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

