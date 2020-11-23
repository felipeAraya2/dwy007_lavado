from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^api/insumos/$',views.InsumosViewSet.as_view()),
    url(r'^api/insumos_f_nombre/(?P<nombre>.+)/$',views.InsumosFiltroNombreViewSet.as_view()),
    url(r'^api/insumos_f_precio/(?P<precio>[0-9]+)/$',views.InsumosFiltroPrecioViewSet.as_view()),

]

urlpatterns=format_suffix_patterns(urlpatterns)