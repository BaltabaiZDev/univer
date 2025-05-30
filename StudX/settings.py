# /StudX_dir/StudX/StudX/settings.py



import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ip7fow8ps=a0el+vgakb42ja+w=_&i)hjou*fxu05$u3mas)k^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [

	'schedule',
	'configuration',
	'communication',
	'common',
	'student',
	'dashboard',
	'widget_tweaks',
	'tinymce',
	'django_makemessages_xgettext',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'user.apps.UserConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'StudX.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'StudX.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'univer',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {'options': '-c timezone=UTC'},  # Критично для Django!
        
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# STATIC_URL = '/static/'

#########################################################################
###                         Custom Section                            ###
#########################################################################

AUTH_USER_MODEL = 'user.User'

#Bootstrap4
BOOTSTRAP4 = {
    'include_jquery': True,
}

# Fixtures
FIXTURE_DIRS = (
   '/fixtures/',
)

# change this to the main dashboard
LOGIN_REDIRECT_URL = 'dashboard:dashboard' 
LOGIN_URL = 'user:login'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_URL = '/home/devdev/StudX_dir/StudX/static/'

MEDIA_URL = '/images/'
MEDIA_ROOT = '/home/devdev/StudX_dir/StudX/images'

### TINYMCE SETTINGS - START ###

TINYMCE_DEFAULT_CONFIG = {
	'height': 360,
	'width': '100%',
	'cleanup_on_startup': True,
	'custom_undo_redo_levels': 20,
	'selector': 'textarea',
	'forced_root_block_attrs': {
		'class': 'mycontent',
		},
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview
            table lists fullscreen  insertdatetime  nonbreaking
            searchreplace wordcount 
            fullscreen autolink lists  print  hr
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline |
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': False,
    'statusbar': True,
	}
	
### TINYMCE SETTINGS - END ###