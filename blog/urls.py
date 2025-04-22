# blog -> urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),  # <- Esto hace que /blog/ funcione
  
    # Vista de inicio, muestra todas las publicaciones
    path('post/list', views.PostListView.as_view(), name='post_list'),

    # Vista para crear una publicación
    path('post/create', views.PostCreateView.as_view(), name='post_create'),

    # Vista para editar una publicación
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),

    # Vista detallada de la publicación
    path('post/detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    # Eliminar una publicación
    path('post/delete/<int:pk>/', views.DeletePostView.as_view(), name='post_delete'),

    # Editar el perfil del usuario
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil/', views.editar_Perfil, name='editar_perfil'),
]

