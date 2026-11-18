
from django.urls import path
from . import views


urlpatterns = [
    # Páginas principales
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),

    # Listado de publicaciones
    path('posts/', views.lista_posts, name='lista_posts'),

    # Crear una publicación
    path('posts/crear/', views.crear_post, name='crear_post'),

    # Ver detalle de una publicación
    path('posts/<int:post_id>/', views.detalle_post, name='detalle_post'),

    # Editar una publicación
    path('posts/<int:post_id>/editar/', views.editar_post, name='editar_post'),

    # Eliminar una publicación
    path('posts/<int:post_id>/eliminar/', views.eliminar_post, name='eliminar_post'),
]
