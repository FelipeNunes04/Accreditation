from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic import *
from django.http import HttpResponseRedirect

from desenvolvedores.models import Desenvolvedor
from desenvolvedores.forms import DesenvolvedorModelForm


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class Home(LoginRequiredMixin, TemplateView):
	template_name = u'index.html'

class DesenvolvedorFormView(LoginRequiredMixin, FormView):
	template_name = 'desenvolvedor/cadastrar.html'
	form_class = DesenvolvedorModelForm
	success_url = reverse_lazy('cadastrar-desenvolvedor')

	def form_valid(self,form):
		jogador = form.save(commit = False)
		if jogador.quentinha_dia1=="Sim" and jogador.carne_dia1=="Nenhuma":
			messages.error(self.request, "Por favor, selecione o tipo de carne da quentinha (1º dia)")
			return self.render_to_response(self.get_context_data(form = form))
		elif jogador.quentinha_dia2=='Sim' and jogador.carne_dia2=='Nenhuma':
			messages.error(self.request, "Por favor, selecione o tipo de carne da quentinha (2º dia)")
			return self.render_to_response(self.get_context_data(form = form))
		else:
			jogador.save()
			messages.success(self.request, "Desenvolvedor cadastrado com sucesso!")
			return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self,form):
		messages.error(self.request, "Por favor, preencha corretamente os campos")
		return self.render_to_response(self.get_context_data(form = form))

class DesenvolvedorListView(LoginRequiredMixin, ListView):
	template_name = 'desenvolvedor/listar.html'

	def get_queryset(self):
		desenvolvedor = Desenvolvedor.objects.all().order_by('equipe')
		return desenvolvedor

class DesenvolvedorUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'desenvolvedor/editar.html'
	model = Desenvolvedor
	form_class = DesenvolvedorModelForm
	success_url = reverse_lazy('listar-desenvolvedor')

	def form_valid(self,form):
		desenvolvedor = form.save(commit = False)
		if desenvolvedor.quentinha_dia1=="Sim" and desenvolvedor.carne_dia1=="Nenhuma":
			messages.error(self.request, "Por favor, selecione o tipo de carne da quentinha (1º dia)")
			return self.render_to_response(self.get_context_data(form = form))
		elif desenvolvedor.quentinha_dia2=='Sim' and desenvolvedor.carne_dia2=='Nenhuma':
			messages.error(self.request, "Por favor, selecione o tipo de carne da quentinha (2º dia)")
			return self.render_to_response(self.get_context_data(form = form))
		else:
			desenvolvedor.save()
			messages.success(self.request, "Desenvolvedor cadastrado com sucesso!")
			return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self,form):
		messages.error(self.request, "Por favor, preencha corretamente os campos")
		return self.render_to_response(self.get_context_data(form = form))

class DesenvolvedorDeleteView(DeleteView):
	template_name = "desenvolvedor/deletar.html"
	model = Desenvolvedor
	success_url = reverse_lazy('listar-desenvolvedor')
	success_message = "Desenvolvedor deletado com sucesso!"

	def delete(self,request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(DesenvolvedorDeleteView, self).delete(request, *args, **kwargs)

