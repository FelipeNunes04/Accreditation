from django.db import models


BOOLEAN_CHOICE = (
	('Não','Não'),
	('Sim','Sim'),
)
CARNES = (
	('Nenhuma','Nenhuma'),
	('Frango Assado','Frango Assado'),
	('Linguiça','Linguiça'),
	('Carne Assada na Brasa','Carne Assada na Brasa'),
	('Galinha','Galinha'),

)
class Jogador(models.Model):
	nome = models.CharField(max_length = 100)
	equipe = models.CharField(max_length = 50)
	presente = models.CharField(max_length = 3, choices=BOOLEAN_CHOICE)
	quentinha_dia1 = models.CharField(max_length = 3, choices=BOOLEAN_CHOICE)
	carne_dia1 = models.CharField(max_length = 30, choices=CARNES)
	quentinha_dia2 = models.CharField(max_length = 3, choices=BOOLEAN_CHOICE)
	carne_dia2 = models.CharField(max_length = 30, choices=CARNES)

		
