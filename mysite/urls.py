"""
mysiteプロジェクトのURL設定。

`urlpatterns`リストはURLをビューにルーティングします。詳細については以下を参照してください：
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
例:
関数ビュー
    1. インポートを追加:  from my_app import views
    2. urlpatternsにURLを追加:  path('', views.home, name='home')
クラスベースのビュー
    1. インポートを追加:  from other_app.views import Home
    2. urlpatternsにURLを追加:  path('', Home.as_view(), name='home')
別のURLconfを含める
    1. include()関数をインポート: from django.urls import include, path
    2. urlpatternsにURLを追加:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)