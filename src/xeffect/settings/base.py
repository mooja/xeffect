"""
"""
from django.core.urlresolvers import reverse_lazy
from os.path import dirname, join, exists

# Build paths inside the project like this: join(BASE_DIR, "directory")
BASE_DIR = dirname(dirname(dirname(__file__)))
STATICFILES_DIRS = [join(BASE_DIR, 'static')]

# Use Django templates using the new Django 1.8 TEMPLATES settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'templates'),
            # insert more TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Use 12factor inspired environment variables or from a file
import environ
env = environ.Env()

env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'authtools',
    'crispy_forms',
    'easy_thumbnails',

    'profiles',
    'accounts',
    'rest_framework',
    'pipeline',

    'habits',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'pipeline.middleware.MinifyHTMLMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

ROOT_URLCONF = 'xeffect.urls'
WSGI_APPLICATION = 'xeffect.wsgi.application'

DATABASES = {
    'default': env.db(),
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = env('STATIC_ROOT')

MEDIA_URL = "/media/"
MEDIA_ROOT = env('MEDIA_ROOT')

ALLOWED_HOSTS = []

# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# For Bootstrap 3, change error alert to 'danger'
from django.contrib import messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Authentication Settings
AUTH_USER_MODEL = 'authtools.User'
LOGIN_REDIRECT_URL = reverse_lazy("profiles:show_self")
LOGIN_URL = reverse_lazy("accounts:login")

THUMBNAIL_EXTENSION = 'png'     # Or any extn for your thumbnails

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}

# use django_pipeline for static file storage
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# sass compiler
PIPELINE_COMPILERS = (
  'pipeline.compilers.sass.SASSCompiler',
  'react.utils.pipeline.JSXCompiler',
)

PIPELINE_CSS = {
  'master': {
    'source_filenames': (
      'bootstrap/css/bootstrap.min.css',
      'bootstrap/css/bootstrap-theme.min.css',
      'site/sass/main.sass',
    ),

    'output_filename': 'site/css/master.css',
      'variant': 'datauri',
    }
}

# pipeline configuration
PIPELINE_JS = {
    'master': {
        'source_filenames': (
          'site/js/src/base/*.js',
        ),
        'output_filename': 'site/js/dist/base.js',
    },
    'habit_detail': {
        'source_filenames': (
            'site/js/src/habit_detail/react.js',
            'site/js/src/habit_detail/components.js',
            'site/js/src/habit_detail/habit_detail.js',
        ),
        'output_filename': 'site/js/dist/habit_detail/habit_detail.js'
    }
}
