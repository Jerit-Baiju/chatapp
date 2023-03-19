from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<int:id>', views.chat, name='chat'),
]
