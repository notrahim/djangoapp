"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from environs import Env
import json
import dj_database_url


env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# settings.py

STATIC_URL = '/static/'



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", default=False)
ALLOWED_HOSTS = ["boiling-ridge-74297-0373cd5fcaf8.herokuapp.com", "localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # "whitenoise.runserver_nostatic",  # new
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third-party
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    #"debug_toolbar",
    # Local
    "accounts.apps.AccountsConfig",
    "pages.apps.PagesConfig",
    "books.apps.BooksConfig",
    "newsletters.apps.NewslettersConfig"
]

MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.security.SecurityMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",  # new
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    #"debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# Default configuration for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'postgres'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        # No password needed for local development with 'trust' authentication
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': '0.0.0.0',  # Matches the service name in docker-compose.yml
        'PORT': '5432',
    }
}

# Override with DATABASE_URL from the environment variable in production (Heroku)
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(default=os.environ.get('DATABASE_URL'))

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# Google Cloud Storage settings -- GIT Commit V2 Google Cloud Storage
# GS_BUCKET_NAME = 'absolutegis'

# # Determine the base directory of your project
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Specify the full path to the service-account-key.json file
# #GS_CREDENTIALS_FILE = os.path.join(BASE_DIR, 'django_project', 'service-account-key.json')

# # Configure Google Cloud Storage credentials using the file path
# #GS_CREDENTIALS = service_account.Credentials.from_service_account_file(GS_CREDENTIALS_FILE)

# # Load credentials from an environment variable
# #GS_CREDENTIALS_JSON = os.environ.get('GS_CREDENTIALS_JSON')
# #if GS_CREDENTIALS_JSON:
# #    GS_CREDENTIALS = service_account.Credentials.from_service_account_info(
# #        json.loads(GS_CREDENTIALS_JSON)
# #    )  


# # Configure Google Cloud Storage credentials
# GS_CREDENTIALS = None

# # Check if the environment variable is set (Heroku)
# GS_CREDENTIALS_JSON = os.environ.get('GS_CREDENTIALS_JSON')
# if GS_CREDENTIALS_JSON:
#     GS_CREDENTIALS = service_account.Credentials.from_service_account_info(
#         json.loads(GS_CREDENTIALS_JSON)
#     )
# else:
#     # Fallback to file-based credentials for local development
#     GS_CREDENTIALS_FILE = os.path.join(BASE_DIR, 'django_project', 'service-account-key.json')
#     if os.path.exists(GS_CREDENTIALS_FILE):
#         GS_CREDENTIALS = service_account.Credentials.from_service_account_file(GS_CREDENTIALS_FILE)





# GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
#    os.path.join(BASE_DIR, 'credentials', 'service-account-key.json')
#)

# Static files (CSS, JavaScript, Images)
# STATIC_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Add this line if you have a 'static' directory in your project
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Temporary local directory for collectstatic
# STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

# # Media files settings
# MEDIA_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/media/'

# DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'


# Default primary key field type - d
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.CustomUser"  # new

# django-crispy-forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"  # new
CRISPY_TEMPLATE_PACK = "bootstrap5"  # new

# django-allauth config
LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT = "home"  # new
SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # new
ACCOUNT_SESSION_REMEMBER = True  # new
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False  # new
ACCOUNT_USERNAME_REQUIRED = False  # new
ACCOUNT_AUTHENTICATION_METHOD = "email"  # new
ACCOUNT_EMAIL_REQUIRED = True  # new
ACCOUNT_UNIQUE_EMAIL = True  # new

DEFAULT_FROM_EMAIL = "admin@djangobookstore.com"  # new

# django-debug-toolbar
#import socket

#hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
#INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]

CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 604800
CACHE_MIDDLEWARE_KEY_PREFIX = ""

SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=False) # change to true before production
SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=2592000)  # 30 days
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", default=True)
CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE", default=True)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")  # new

#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  # new
