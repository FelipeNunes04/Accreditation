from django.conf.urls import  url
from relatorios.views import *

urlpatterns = [
	url(r'^jogadores/$', jogadores_credenciados, name="jogadores-credenciados"),
	url(r'^espectadores/$', espectadores_credenciados, name="espectadores-credenciados"),
	url(r'^quentinhas/$', quentinhas, name="quentinhas"),
]