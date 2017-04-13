"""dj_ueditor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf.urls.static import static
from django.views import  static as static_file
import  demo.views as v
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',v.index),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^detail/(\d+)/$',v.detail),
    url(r'^static/(?P<path>.*)$', static_file.serve, {'document_root': settings.STATIC_ROOT}),
]+ static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)