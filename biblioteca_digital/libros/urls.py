from django.urls import path
from . import views
from .views import lista_libros, baja_libro, editar_libro
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),  # Página principal o listado de libros
    path('alta-inventario/', views.alta_inventario, name='alta_inventario'),  # Ruta para dar de alta en inventario
    path('alta-libro/', views.alta_libro, name='alta_libro'),  # Ruta para dar de alta un libro
    path('libros/baja/', baja_libro, name='baja_libro'),  # Nueva ruta
    path('editar-libro/<int:libro_id>/', editar_libro, name='editar_libro')  # Cambiado para aceptar libro_id
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)