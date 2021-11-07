"""trainersdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path,include
from filebrowser.sites import site
from wagtail.core import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    # path('admin/filebrowser/',  site.urls),
    # path('grappelli/', include('grappelli.urls')),
    path('django-admin/', admin.site.urls),
    path('apiauthentication/', include('rest_framework.urls')),
    path('api/',include('trainerspro.urls')),
    path('debug/', include(debug_toolbar.urls,namespace='django_toolbar')),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls))
    # path('mce_filebrowser/',include('mce_filebrowser.urls'))
]
