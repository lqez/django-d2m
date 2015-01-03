DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_d2m.db',
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

STATIC_URL = '/'
SECRET_KEY = 'django_d2m'

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'django_d2m.testapp',
)
