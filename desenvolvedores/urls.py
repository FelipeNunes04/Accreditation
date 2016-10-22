from django.conf.urls import  url
from desenvolvedores.views import *


urlpatterns = [
    url(r'^desenvolvedor/cadastrar/$',DesenvolvedorFormView.as_view(), name = 'cadastrar-desenvolvedor'),
    url(r'^desenvolvedor/listar/$',DesenvolvedorListView.as_view(), name = 'listar-desenvolvedor'),
    url(r'^desenvolvedor/(?P<pk>[\w-]+)/atualizar$',DesenvolvedorUpdateView.as_view(), name = 'update-desenvolvedor'),
    url(r'^desenvolvedor/(?P<pk>[\w-]+)/deletar/$',DesenvolvedorDeleteView.as_view(), name = 'delete-desenvolvedor'),

]