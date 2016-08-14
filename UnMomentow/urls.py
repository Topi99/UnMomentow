from django.conf.urls import urls, include
from django.contrib import admin
from main import urls as UrlsMain

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^/', include(UrlsMain, namespace="main")),
]
