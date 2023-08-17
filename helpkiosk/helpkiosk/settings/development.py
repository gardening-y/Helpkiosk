from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# True, False 상관없음

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DEBUG=True일 경우
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# False일 경우 
# STATIC_ROOT = BASE_DIR / 'static'