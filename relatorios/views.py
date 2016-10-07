from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jogadores.models import Jogador
from espectadores.models import Espectador

preco_venda_quentinha = 10.00
preco_compra_quentinha = 8.70

@login_required
def jogadores_credenciados(request):
	todos_jogadores = Jogador.objects.all()
	jogadores_presentes = Jogador.objects.filter(presente = 'Sim')
	jogadores_quentinha_dia1 = Jogador.objects.filter(quentinha_dia1 = 'Sim')
	jogadores_quentinha_dia1_frango = Jogador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Frango Assado")
	jogadores_quentinha_dia1_linguica = Jogador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Linguiça")
	jogadores_quentinha_dia1_carne = Jogador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Carne Assada na Brasa")
	jogadores_quentinha_dia1_galinha = Jogador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Galinha")

	jogadores_quentinha_dia2 = Jogador.objects.filter(quentinha_dia2 = 'Sim')
	jogadores_quentinha_dia2_frango = Jogador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Frango Assado")
	jogadores_quentinha_dia2_linguica = Jogador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Linguiça")
	jogadores_quentinha_dia2_carne = Jogador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Carne Assada na Brasa")
	jogadores_quentinha_dia2_galinha = Jogador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Galinha")
	
	num_jogadores = todos_jogadores.count()
	num_jogadores_presentes = jogadores_presentes.count()
	
	num_jogadores_quentinha_dia1 = jogadores_quentinha_dia1.count()
	num_jogadores_quentinha_dia1_frango = jogadores_quentinha_dia1_frango.count()
	num_jogadores_quentinha_dia1_linguica = jogadores_quentinha_dia1_linguica.count()
	num_jogadores_quentinha_dia1_carne = jogadores_quentinha_dia1_carne.count()
	num_jogadores_quentinha_dia1_galinha = jogadores_quentinha_dia1_galinha.count()

	num_jogadores_quentinha_dia2 = jogadores_quentinha_dia2.count()
	num_jogadores_quentinha_dia2_frango = jogadores_quentinha_dia2_frango.count()
	num_jogadores_quentinha_dia2_linguica = jogadores_quentinha_dia2_linguica.count()
	num_jogadores_quentinha_dia2_carne = jogadores_quentinha_dia2_carne.count()
	num_jogadores_quentinha_dia2_galinha = jogadores_quentinha_dia2_galinha.count()

	num_jogadores_quentinha_total = num_jogadores_quentinha_dia1 + num_jogadores_quentinha_dia2
	valor_total_jogadores_venda = num_jogadores_quentinha_total * preco_venda_quentinha

	return render(request, 'jogadores_credenciados/count.html', {"num_jogadores" : num_jogadores,
	 "num_jogadores_presentes": num_jogadores_presentes,"num_jogadores_quentinha_dia1":num_jogadores_quentinha_dia1,
	 "num_jogadores_quentinha_dia2":num_jogadores_quentinha_dia2,"num_jogadores_quentinha_total":num_jogadores_quentinha_total,
	 "valor_total_jogadores_venda":valor_total_jogadores_venda,"num_jogadores_quentinha_dia1_frango":num_jogadores_quentinha_dia1_frango,
	 "num_jogadores_quentinha_dia1_linguica":num_jogadores_quentinha_dia1_linguica,"num_jogadores_quentinha_dia1_carne":num_jogadores_quentinha_dia1_carne,
	 "num_jogadores_quentinha_dia1_galinha":num_jogadores_quentinha_dia1_galinha,"num_jogadores_quentinha_dia2_frango":num_jogadores_quentinha_dia2_frango,
	 "num_jogadores_quentinha_dia2_linguica":num_jogadores_quentinha_dia2_linguica,"num_jogadores_quentinha_dia2_carne":num_jogadores_quentinha_dia2_carne,
	 "num_jogadores_quentinha_dia2_galinha":num_jogadores_quentinha_dia2_galinha,
	 })

@login_required
def espectadores_credenciados(request):
	espectadores_presentes_dia1 = Espectador.objects.filter(presente_dia1 = 'Sim')
	espectadores_presentes_dia2 = Espectador.objects.filter(presente_dia2 = 'Sim')
	
	espectadores_quentinha_dia1 = Espectador.objects.filter(quentinha_dia1 = 'Sim')
	espectadores_quentinha_dia1_frango = Espectador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Frango Assado")
	espectadores_quentinha_dia1_linguica = Espectador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Linguiça")
	espectadores_quentinha_dia1_carne = Espectador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Carne Assada na Brasa")
	espectadores_quentinha_dia1_galinha = Espectador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Galinha")

	espectadores_quentinha_dia2 = Espectador.objects.filter(quentinha_dia2 = 'Sim')
	espectadores_quentinha_dia2_frango = Espectador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Frango Assado")
	espectadores_quentinha_dia2_linguica = Espectador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Linguiça")
	espectadores_quentinha_dia2_carne = Espectador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Carne Assada na Brasa")
	espectadores_quentinha_dia2_galinha = Espectador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Galinha")

	num_espectadores_quentinha_dia1 = espectadores_quentinha_dia1.count()
	num_espectadores_quentinha_dia1_frango = espectadores_quentinha_dia1_frango.count()
	num_espectadores_quentinha_dia1_linguica = espectadores_quentinha_dia1_linguica.count()
	num_espectadores_quentinha_dia1_carne = espectadores_quentinha_dia1_carne.count()
	num_espectadores_quentinha_dia1_galinha = espectadores_quentinha_dia1_galinha.count()

	num_espectadores_quentinha_dia2 = espectadores_quentinha_dia2.count()
	num_espectadores_quentinha_dia2_frango = espectadores_quentinha_dia2_frango.count()
	num_espectadores_quentinha_dia2_linguica = espectadores_quentinha_dia2_linguica.count()
	num_espectadores_quentinha_dia2_carne = espectadores_quentinha_dia2_carne.count()
	num_espectadores_quentinha_dia2_galinha = espectadores_quentinha_dia2_galinha.count()

	num_espectadores_quentinha_total = num_espectadores_quentinha_dia1 + num_espectadores_quentinha_dia2
	valor_total_espectadores_venda = num_espectadores_quentinha_total * preco_venda_quentinha
	
	num_espectadores_presentes_dia1 = espectadores_quentinha_dia1.count()
	num_espectadores_presentes_dia2 = espectadores_presentes_dia2.count()
	num_espectadores_total = num_espectadores_presentes_dia1 + num_espectadores_presentes_dia2

	return render(request, 'espectadores_credenciados/count.html', {"num_espectadores_presentes_dia1":num_espectadores_presentes_dia1,
	 "num_espectadores_presentes_dia2":num_espectadores_presentes_dia2,"num_espectadores_quentinha_dia1":num_espectadores_quentinha_dia1, 
	 "num_espectadores_quentinha_dia2":num_espectadores_quentinha_dia2,"num_espectadores_quentinha_total": num_espectadores_quentinha_total,
	 "valor_total_espectadores_venda":valor_total_espectadores_venda,"num_espectadores_quentinha_dia1_frango":num_espectadores_quentinha_dia1_frango,
	 "num_espectadores_quentinha_dia1_linguica":num_espectadores_quentinha_dia1_linguica,"num_espectadores_quentinha_dia1_carne":num_espectadores_quentinha_dia1_carne,
	 "num_espectadores_quentinha_dia1_galinha":num_espectadores_quentinha_dia1_galinha,"num_espectadores_quentinha_dia2_frango":num_espectadores_quentinha_dia2_frango,
	 "num_espectadores_quentinha_dia2_linguica":num_espectadores_quentinha_dia2_linguica,"num_espectadores_quentinha_dia2_carne":num_espectadores_quentinha_dia2_carne,
	 "num_espectadores_quentinha_dia2_galinha":num_espectadores_quentinha_dia2_galinha,
	 })

@login_required
def quentinhas(request):
	#jogadores
	todos_jogadores = Jogador.objects.all()
	jogadores_presentes = Jogador.objects.filter(presente = 'Sim')
	
	jogadores_quentinha_dia1 = Jogador.objects.filter(quentinha_dia1 = 'Sim')
	jogadores_quentinha_dia1_frango = Jogador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Frango Assado")
	jogadores_quentinha_dia1_linguica = Jogador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Linguiça")
	jogadores_quentinha_dia1_carne = Jogador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Carne Assada na Brasa")
	jogadores_quentinha_dia1_galinha = Jogador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Galinha")

	jogadores_quentinha_dia2 = Jogador.objects.filter(quentinha_dia2 = 'Sim')
	jogadores_quentinha_dia2_frango = Jogador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Frango Assado")
	jogadores_quentinha_dia2_linguica = Jogador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Linguiça")
	jogadores_quentinha_dia2_carne = Jogador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Carne Assada na Brasa")
	jogadores_quentinha_dia2_galinha = Jogador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Galinha")

	num_jogadores = todos_jogadores.count()
	num_jogadores_presentes = jogadores_presentes.count()
	
	num_jogadores_quentinha_dia1 = jogadores_quentinha_dia1.count()
	num_jogadores_quentinha_dia1_frango = jogadores_quentinha_dia1_frango.count()
	num_jogadores_quentinha_dia1_linguica = jogadores_quentinha_dia1_linguica.count()
	num_jogadores_quentinha_dia1_carne = jogadores_quentinha_dia1_carne.count()
	num_jogadores_quentinha_dia1_galinha = jogadores_quentinha_dia1_galinha.count()

	num_jogadores_quentinha_dia2 = jogadores_quentinha_dia2.count()
	num_jogadores_quentinha_dia2_frango = jogadores_quentinha_dia2_frango.count()
	num_jogadores_quentinha_dia2_linguica = jogadores_quentinha_dia2_linguica.count()
	num_jogadores_quentinha_dia2_carne = jogadores_quentinha_dia2_carne.count()
	num_jogadores_quentinha_dia2_galinha = jogadores_quentinha_dia2_galinha.count()

	num_jogadores_quentinha_total = num_jogadores_quentinha_dia1 + num_jogadores_quentinha_dia2
	#espectadores
	todos_espectadores = Espectador.objects.all()
	espectadores_quentinha_dia1 = Espectador.objects.filter(quentinha_dia1 = 'Sim')
	espectadores_quentinha_dia1_frango = Espectador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Frango Assado")
	espectadores_quentinha_dia1_linguica = Espectador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Linguiça")
	espectadores_quentinha_dia1_carne = Espectador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Carne Assada na Brasa")
	espectadores_quentinha_dia1_galinha = Espectador.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Galinha")

	espectadores_quentinha_dia2 = Espectador.objects.filter(quentinha_dia2 = 'Sim')
	espectadores_quentinha_dia2_frango = Espectador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Frango Assado")
	espectadores_quentinha_dia2_linguica = Espectador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Linguiça")
	espectadores_quentinha_dia2_carne = Espectador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Carne Assada na Brasa")
	espectadores_quentinha_dia2_galinha = Espectador.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Galinha")

	espectadores_presentes_dia1 = Espectador.objects.filter(presente_dia1 = 'Sim')
	espectadores_presentes_dia2 = Espectador.objects.filter(presente_dia2 = 'Sim')
	
	num_espectadores = todos_espectadores.count()
	num_espectadores_quentinha_dia1 = espectadores_quentinha_dia1.count()
	num_espectadores_quentinha_dia1_frango = espectadores_quentinha_dia1_frango.count()
	num_espectadores_quentinha_dia1_linguica = espectadores_quentinha_dia1_linguica.count()
	num_espectadores_quentinha_dia1_carne = espectadores_quentinha_dia1_carne.count()
	num_espectadores_quentinha_dia1_galinha = espectadores_quentinha_dia1_galinha.count()

	num_espectadores_quentinha_dia2 = espectadores_quentinha_dia2.count()
	num_espectadores_quentinha_dia2_frango = espectadores_quentinha_dia2_frango.count()
	num_espectadores_quentinha_dia2_linguica = espectadores_quentinha_dia2_linguica.count()
	num_espectadores_quentinha_dia2_carne = espectadores_quentinha_dia2_carne.count()
	num_espectadores_quentinha_dia2_galinha = espectadores_quentinha_dia2_galinha.count()

	num_espectadores_quentinha_total = num_espectadores_quentinha_dia1 + num_espectadores_quentinha_dia2

	num_espectadores_presentes_dia1 = espectadores_presentes_dia1.count()
	num_espectadores_presentes_dia2 = espectadores_presentes_dia2.count()
	num_espectadores_presentes_total = num_espectadores_presentes_dia1 + num_espectadores_presentes_dia2
	#total de participantes e de quentinhas
	num_total_participantes = num_jogadores + num_espectadores
	num_total_participantes_presentes = num_jogadores_presentes + num_espectadores_presentes_total

	num_total_quentinhas = num_jogadores_quentinha_total + num_espectadores_quentinha_total

	num_total_quentinhas_dia1 = num_jogadores_quentinha_dia1 + num_espectadores_quentinha_dia1
	num_total_quentinhas_dia1_frango = num_espectadores_quentinha_dia1_frango + num_jogadores_quentinha_dia1_frango
	num_total_quentinhas_dia1_linguica = num_espectadores_quentinha_dia1_linguica + num_jogadores_quentinha_dia1_linguica
	num_total_quentinhas_dia1_carne = num_espectadores_quentinha_dia1_carne + num_jogadores_quentinha_dia1_carne
	num_total_quentinhas_dia1_galinha = num_espectadores_quentinha_dia1_galinha + num_jogadores_quentinha_dia1_galinha

	num_total_quentinhas_dia2 = num_jogadores_quentinha_dia2 + num_espectadores_quentinha_dia2
	num_total_quentinhas_dia2_frango = num_espectadores_quentinha_dia2_frango + num_jogadores_quentinha_dia2_frango
	num_total_quentinhas_dia2_linguica = num_espectadores_quentinha_dia2_linguica + num_jogadores_quentinha_dia2_linguica
	num_total_quentinhas_dia2_carne = num_espectadores_quentinha_dia2_carne + num_jogadores_quentinha_dia2_carne
	num_total_quentinhas_dia2_galinha = num_espectadores_quentinha_dia2_galinha + num_jogadores_quentinha_dia2_galinha
	#preço da quentinha
	valor_total_venda = num_total_quentinhas * preco_venda_quentinha
	valor_total_compra =  num_total_quentinhas * preco_compra_quentinha
	valor_total_lucro = valor_total_venda - valor_total_compra

	return render(request, 'quentinhas/count.html', {"num_total_participantes":num_total_participantes,  "num_total_participantes_presentes": num_total_participantes_presentes,
	 "num_total_quentinhas_dia1":num_total_quentinhas_dia1,"num_total_quentinhas_dia2":num_total_quentinhas_dia2,
	 "num_total_quentinhas_dia1_frango":num_total_quentinhas_dia1_frango,"num_total_quentinhas_dia1_linguica":num_total_quentinhas_dia1_linguica,
	 "num_total_quentinhas_dia1_carne":num_total_quentinhas_dia1_carne,"num_total_quentinhas_dia1_galinha":num_total_quentinhas_dia1_galinha,
	 "num_total_quentinhas_dia2_frango":num_total_quentinhas_dia2_frango,"num_total_quentinhas_dia2_linguica":num_total_quentinhas_dia2_linguica,
	 "num_total_quentinhas_dia2_carne":num_total_quentinhas_dia2_carne,"num_total_quentinhas_dia2_galinha":num_total_quentinhas_dia2_galinha,
	 "num_total_quentinhas":num_total_quentinhas, "preco_venda_quentinha":preco_venda_quentinha,
	 "preco_compra_quentinha":preco_compra_quentinha,"valor_total_venda":valor_total_venda,
	 "valor_total_compra": valor_total_compra, "valor_total_lucro":valor_total_lucro
	 })
