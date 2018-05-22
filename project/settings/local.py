from os import path
from decouple import config

from dj_database_url import parse

from .base import *  # noqa


DEBUG = True

SECRET_KEY = 'ABCDEFG1234567890'

DATABASES = {
    'default': parse(config('DATABASE_URL', default='sqlite:///' + path.join(BASE_DIR, 'db.sqlite3'))),
}
