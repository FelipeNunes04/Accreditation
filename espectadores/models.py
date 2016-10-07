from django.db import models
from jogadores.models import BOOLEAN_CHOICE, CARNES

class Espectador(models.Model):
	nome = models.CharField(max_length = 100)
	quentinha_dia1 = models.CharField(max_length=3, choices=BOOLEAN_CHOICE)
	carne_dia1 = models.CharField(max_length = 30, choices=CARNES)
	quentinha_dia2 = models.CharField(max_length=3, choices=BOOLEAN_CHOICE)
	carne_dia2 = models.CharField(max_length = 30, choices=CARNES)
	presente_dia1 = models.CharField(max_length = 3, choices=BOOLEAN_CHOICE)
	presente_dia2 = models.CharField(max_length = 3, choices=BOOLEAN_CHOICE)

