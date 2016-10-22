from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.auth.views import login,logout

from desenvolvedores.views import Home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^desenvolvedor/', include('desenvolvedores.urls')),
    url(r'^relatorio/', include('relatorios.urls')),

    url(r'^$', Home.as_view(), name='home'),
    url(r'^usuario/login/$',login,{'template_name':'autenticacao/login.html'},name='login'),
    url(r'^usuario/logout/$',logout,{'template_name':'autenticacao/logout.html'},name='logout'),
]
