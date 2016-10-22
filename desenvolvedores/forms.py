# -*- coding: utf-8 -*-

from django import forms
from desenvolvedores.models import *

class DesenvolvedorModelForm(forms.ModelForm):
	nome = forms.CharField(
		label = "Nome do Desenvolvedor",
		widget = forms.TextInput(
			attrs = {
				'placeholder': 'Nome do Desenvolvedor',
				'required': 'required',
				'class': 'form-control'
			}
		)
	)
	equipe = forms.CharField(
		label = "Equipe",
		widget = forms.TextInput(
			attrs = {
				'placeholder': 'Nome da Equipe',
				'required': 'required',
				'class': 'form-control'
			}
		)
	)
	presente = forms.ChoiceField(
		label = 'Presente', 
		choices=BOOLEAN_CHOICE,
	)
	quentinha_dia1 = forms.ChoiceField(
		label = 'Quentinha (1º dia)', 
		choices=BOOLEAN_CHOICE,
	)
	carne_dia1 = forms.ChoiceField(
		label = 'Tipo da Carne (1º dia)', 
		choices=CARNES,
	)
	quentinha_dia2 = forms.ChoiceField(
		label = 'Quentinha (2º dia)', 
		choices=BOOLEAN_CHOICE,
	)
	carne_dia2 = forms.ChoiceField(
		label = 'Tipo da Carne (2º dia)', 
		choices=CARNES,
	)

	class Meta:
		model = Desenvolvedor
		fields = ('nome','equipe','presente','quentinha_dia1','carne_dia1','quentinha_dia2','carne_dia2')