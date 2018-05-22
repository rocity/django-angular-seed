from os import path
from dj_database_url import parse

from .common import *  # noqa


DATABASES = {
    'default': parse(config('DATABASE_URL')),
}

STATICFILES_DIRS = [
    path.join(BASE_DIR, 'assets', 'dist')
]
