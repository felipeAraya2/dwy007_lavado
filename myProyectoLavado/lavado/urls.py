from django.contrib import admin
from django.urls import path, include
from .views import busqueda_prod,formulario,galeria,index,producto,quienes,servicios,login,cerrar_sesion, lista_producto,eliminar,modificar

urlpatterns = [
    path('',index,name='IND'),
    path('galeria',galeria,name='GALE'),
    path('formulario',formulario,name='FORM'),
    path('producto',producto, name='PROD'),
    path('quienes-somos',quienes, name='QUIE'),
    path('servicios', servicios, name='SERV'),
    path('login',login, name='LOGIN'),
    path('cerrar_sesion',cerrar_sesion, name='LOGOUT'),
    path('lista_producto/', lista_producto, name='LISTAPROD'),
    path('eliminar/<id>/',eliminar, name='ELIMINAR'),
    path('buscar/<id>/',busqueda_prod,name='BUSCAR'),
    path('modificar',modificar,name='MOD'),
    path('oauth/', include('social_django.urls', namespace='social'))

]
