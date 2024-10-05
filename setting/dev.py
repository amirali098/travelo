
# SECURITY WARNING: keep the secret key used in production secret!


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-teb@vxvo8v4l9%2j46bl7+tkz8kg!8borahdz13vq8a6(@+bfl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
SITE_ID = 2



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'


STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


X_FRAME_OPTIONS = "SAMEORIGIN"
CSRF_COOKIE_SECURE=True