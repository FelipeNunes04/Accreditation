from django.conf.urls import  url
from jogadores.views import *


urlpatterns = [
    url(r'^jogador/cadastrar/$',JogadorFormView.as_view(), name = 'cadastrar-jogador'),
    url(r'^jogador/listar/$',JogadorListView.as_view(), name = 'listar-jogador'),
    url(r'^jogador/(?P<pk>[\w-]+)/atualizar$',JogadorUpdateView.as_view(), name = 'update-jogador'),
    url(r'^jogador/(?P<pk>[\w-]+)/deletar/$',JogadorDeleteView.as_view(), name = 'delete-jogador'),

]