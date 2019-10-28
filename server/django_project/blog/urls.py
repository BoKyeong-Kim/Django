from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<int:id>/',views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'), 
]
