from django.urls import path
from . import views

urlpatterns=[
    path('', views.post_list, name='post_list'),
    path('post/my', views.post_my, name='my_posts'),
    path('post/add', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
]