"""
mysiteプロジェクトのDjango設定。

Django 4.2.17を使用して'django-admin startproject'によって生成されました。

このファイルの詳細については、
https://docs.djangoproject.com/en/4.2/topics/settings/ を参照してください。

設定とその値の完全なリストについては、
https://docs.djangoproject.com/en/4.2/ref/settings/ を参照してください。
"""

from pathlib import Path
import os                 # 手動で追加

# プロジェクト内のパスをこのように構築します: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# 開発用のクイックスタート設定 - 本番環境には不適切
# 詳細は https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/ を参照してください

# セキュリティ警告: 本番環境では使用するシークレットキーを秘密にしてください!
SECRET_KEY = 'django-insecure-9p&*019*ng!mi+r4+52^dhsdgp!@=f24w6n2xt_u5kewzv7kfy'

# セキュリティ警告: 本番環境ではデバッグをオンにしないでください!
DEBUG = True

ALLOWED_HOSTS = []


# アプリケーション定義

INSTALLED_APPS = [
    'core.apps.CoreConfig',          # 手動で追加
    'accounts.apps.AccountsConfig',  # 手動で追加
    'bootstrap5',                    # 手動で追加
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],  # 手動で追加
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# データベース
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {  # 手動で変更
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'django',
        'PASSWORD': 'djangopassword',
        'HOST': 'db',
        'PORT': '3306',
    }
}

# パスワード検証
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# 国際化
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ja'  # 手動で変更

TIME_ZONE = 'Asia/Tokyo'  # 手動で変更

USE_I18N = True

USE_TZ = True


# 静的ファイル (CSS、JavaScript、画像)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'  # 手動で追加
STATICFILES_DIRS = [    # 手動で追加
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'                         # 手動で追加
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 手動で追加


# デフォルトのプライマリキーのフィールドタイプ
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'accounts.CustomUser'  # 手動で追加


# ログインURL
LOGIN_URL = '/accounts/login/'            # 手動で追加
# ログイン後のリダイレクト先
LOGIN_REDIRECT_URL = '/'                  # 手動で追加
# ログアウト後のリダイレクト先
LOGOUT_REDIRECT_URL = '/accounts/login/'  # 手動で追加
