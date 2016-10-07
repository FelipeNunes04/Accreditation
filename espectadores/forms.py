# -*- coding: utf-8 -*-

from django import forms
from .models import Espectador
from jogadores.models import BOOLEAN_CHOICE, CARNES

class EspectadorModelForm(forms.ModelForm):
	nome = forms.CharField(
		label = "Nome do Espectador",
		widget = forms.TextInput(
			attrs = {
				'placeholder': 'Nome do Espectador',
				'required': 'required',
				'class': 'form-control'
			}
		)
	)
	quentinha_dia1 = forms.ChoiceField(
		label = 'Quentinha (1º dia)', 
		choices = BOOLEAN_CHOICE,
	)
	carne_dia1 = forms.ChoiceField(
		label = 'Tipo da Carne (1º dia)', 
		choices=CARNES,
	)
	quentinha_dia2 = forms.ChoiceField(
		label = 'Quentinha (2º dia)', 
		choices = BOOLEAN_CHOICE,
	)
	carne_dia2 = forms.ChoiceField(
		label = 'Tipo da Carne (2º dia)', 
		choices=CARNES,
	)
	presente_dia1 = forms.ChoiceField(
		label = 'Presente (1º dia)', 
		choices=BOOLEAN_CHOICE,
	)
	presente_dia2 = forms.ChoiceField(
		label = 'Presente (2º dia)', 
		choices=BOOLEAN_CHOICE,
	)

	class Meta:
		model = Espectador 
		fields = ('nome','presente_dia1','presente_dia2','quentinha_dia1','carne_dia1','quentinha_dia2','carne_dia2')