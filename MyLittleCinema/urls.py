from django.urls import path
from myLittleCinemaApp import views

urlpatterns = [
    path('create/', views.create_movie, name='create_movie'),
    path('get/', views.get_movie, name='get_movie'),
    path('update/', views.update_movie, name='update_movie'),
    path('delete/', views.delete_movie, name='delete_movie'),
]
