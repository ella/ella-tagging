from os.path import dirname, join, normpath, pardir

FILE_ROOT = normpath(join(dirname(__file__), pardir))

USE_I18N = True

MEDIA_ROOT = join(FILE_ROOT, 'static')


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'test_ella.template_loader.load_template_source',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'test_ella_tagging.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(FILE_ROOT, 'templates'),

)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.core.context_processors.auth',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.admin',
    'django.contrib.comments',

    'tagging',

    'ella.core',
    'ella.photos',
    'ella.articles',
    'ella_tagging',
)

TAG_LISTINGS_PAGINATE_BY = 1

RELATED_FINDERS = {
    'default': (
        'ella.core.related_finders.directly_related',
        'ella_tagging.related_finders.related_by_tags',
        'ella.core.related_finders.related_by_category',
    )
}

