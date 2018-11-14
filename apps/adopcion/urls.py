from django.urls import path
from . import views
from apps.adopcion.views import SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    path('listar', SolicitudList.as_view(), name='solicitud_listar'),
    path('nuevo', SolicitudCreate.as_view(), name='solicitud_crear'),
    path('editar/<pk>', SolicitudUpdate.as_view(), name='solicitud_editar'),
    path('eliminar/<pk>', SolicitudDelete.as_view(), name='solicitud_eliminar'),
]


