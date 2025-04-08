from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # <- Esto hace que /blog/ funcione
    path('post/list', views.post_list, name='post_list'),
    path('post/create', views.post_create, name='post_create'),
]
