from django.conf.urls import  url
from espectadores.views import *


urlpatterns = [
    url(r'^espectador/cadastrar/$',EspectadorFormView.as_view(), name = 'cadastrar-espectador'),
    url(r'^espectador/listar/$',EspectadorListView.as_view(), name = 'listar-espectador'),
    url(r'^espectador/(?P<pk>[\w-]+)/atualizar$',EspectadorUpdateView.as_view(), name = 'update-espectador'),
    url(r'^espectador/(?P<pk>[\w-]+)/deletar/$',EspectadorDeleteView.as_view(), name = 'delete-espectador'),

]