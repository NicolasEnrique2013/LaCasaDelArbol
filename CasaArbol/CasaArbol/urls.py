"""CasaArbol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, re_path, include
from apps.noticias import views
from apps.login import views
from apps.eventos import views
from apps.contacto import views,urls
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contacto/',views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('proyectos/',views.proyecto, name='proyecto'),
    path('',include ('apps.login.urls')),
    path('donar/', views.donar, name='donar'),
    path('accounts/', include('django.contrib.auth.urls') )
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve ,{
            'document_root':settings.MEDIA_ROOT,
            })
    ]
