from django.conf.urls import include, url
import views

"""
    Tipo de indentificacion
"""

urlpatterns = [
    url(r'^tipo/form/$', views.TipoSupraForm.as_view(), name="tipo"),
    url(r'^tipo/list/$', views.TipoList.as_view(), name="tipo_list"),
    url(r'^tipo/form/(?P<pk>\d+)/$',
        views.TipoSupraForm.as_view(), name="tipo_edit"),
    url(r'^tipo/delete/(?P<pk>\d+)/$',
        views.TipoDeleteSupra.as_view(), name="tipo_delete"),
]