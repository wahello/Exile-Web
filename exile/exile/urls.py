"""exile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('frontend.urls')),
    url(r'^usuarios/', include('usuarios.urls')),
    url(r'^novedades/', include('novedades.urls')),
    url(r'^chat/', include('chat.urls')),
    url(r'^subscripcion/', include('subcripcion.urls', namespace='suscripcion')),
    url(r'^operacion/', include('operacion.urls', namespace='operacion')),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
