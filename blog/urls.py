from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # <- Esto hace que /blog/ funcione
    #path('post/list', views.post_list, name='post_list'),
    path('post/list', views.PostListView.as_view(), name='post_list'),
    path('post/create', views.post_create, name='post_create'),
    path('post/detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/delete/<int:pk>/', views.DeletePostView.as_view(), name='post_delete'),
]
