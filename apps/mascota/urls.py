from django.urls import path
from . import views
from apps.mascota.views import MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete
urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo',MascotaCreate.as_view(), name='mascota_crear'),
    path('listar',MascotaList.as_view(), name='mascota listar'),
    path('editar/<pk>/', MascotaUpdate.as_view(), name='mascota_editar'),
    path('eliminar/<pk>/', MascotaDelete.as_view(), name='mascota_eliminar')

]
