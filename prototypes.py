import os
import sys
from django.conf import settings

BASE_DIR = os.path.dirname('__file__')
print(BASE_DIR)

settings.configure(
        DEBUG=True,
        SECRET_KEY='b0mqvak1p2sqm6p#+8o8fyxf+ox(le)8&jh_5^sxa!=7!+wxj0',
        ROOT_URLCONF='sitebuilder.urls',
        MIDDLEWARE_CLASSES=(),
        INSTALLED_APPS=(
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'django.contrib.staticfiles',
            'django.contrib.webdesign',
            'sitebuilder',
        ),
        STATIC_URL='/static/',
        SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

