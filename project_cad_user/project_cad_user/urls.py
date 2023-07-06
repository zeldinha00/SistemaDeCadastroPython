from django.urls import path
from app_cad_user import views

urlpatterns = [
    #rota, view responsável, nome de referencia ('' vazia pois é a pagina inicial)
    path('', views.home, name='home'),

    #rota para pagina com dados dos usuário
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
