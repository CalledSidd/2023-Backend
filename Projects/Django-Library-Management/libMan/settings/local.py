from pathlib import Path
from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = True

SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}