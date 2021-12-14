from django.urls import path
from .views import *

urlpatterns = [
    path('listar', listar_users, name='listar_users'),
    path('cadastrar', cadastrar_users, name='cadastrar_users'),
    path('listar/<int:id>',listar_user_id, name='listar_user_id'),
    path('editar/<int:id>',editar_user, name='editar_user'),
    path('remover/<int:id>',remover_user, name='remover_user')
]