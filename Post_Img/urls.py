from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_img, name='posts_img'),
]
