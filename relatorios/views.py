from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from desenvolvedores.models import Desenvolvedor

preco_venda_quentinha = 10.00
preco_compra_quentinha = 8.50

@login_required
def quentinhas(request):
	#jogadores
	todos_jogadores = Desenvolvedor.objects.all()
	jogadores_presentes = Desenvolvedor.objects.filter(presente = 'Sim')
	
	jogadores_quentinha_dia1 = Desenvolvedor.objects.filter(quentinha_dia1 = 'Sim')
	jogadores_quentinha_dia1_frango = Desenvolvedor.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Frango Assado")
	jogadores_quentinha_dia1_linguica = Desenvolvedor.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Linguiça")
	jogadores_quentinha_dia1_carne = Desenvolvedor.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Carne Assada na Brasa")
	jogadores_quentinha_dia1_galinha = Desenvolvedor.objects.filter(quentinha_dia1 = 'Sim', carne_dia1="Galinha")

	jogadores_quentinha_dia2 = Desenvolvedor.objects.filter(quentinha_dia2 = 'Sim')
	jogadores_quentinha_dia2_frango = Desenvolvedor.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Frango Assado")
	jogadores_quentinha_dia2_linguica = Desenvolvedor.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Linguiça")
	jogadores_quentinha_dia2_carne = Desenvolvedor.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Carne Assada na Brasa")
	jogadores_quentinha_dia2_galinha = Desenvolvedor.objects.filter(quentinha_dia2 = 'Sim', carne_dia2="Galinha")

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
	
	#total de participantes e de quentinhas
	num_total_participantes = num_jogadores
	num_total_participantes_presentes = num_jogadores_presentes

	num_total_quentinhas = num_jogadores_quentinha_total

	num_total_quentinhas_dia1 = num_jogadores_quentinha_dia1
	num_total_quentinhas_dia1_frango = num_jogadores_quentinha_dia1_frango
	num_total_quentinhas_dia1_linguica = num_jogadores_quentinha_dia1_linguica
	num_total_quentinhas_dia1_carne = num_jogadores_quentinha_dia1_carne
	num_total_quentinhas_dia1_galinha = num_jogadores_quentinha_dia1_galinha

	num_total_quentinhas_dia2 = num_jogadores_quentinha_dia2
	num_total_quentinhas_dia2_frango = num_jogadores_quentinha_dia2_frango
	num_total_quentinhas_dia2_linguica = num_jogadores_quentinha_dia2_linguica
	num_total_quentinhas_dia2_carne = num_jogadores_quentinha_dia2_carne
	num_total_quentinhas_dia2_galinha = num_jogadores_quentinha_dia2_galinha
	#preço da quentinha
	valor_venda_dia1 = num_total_quentinhas_dia1 * preco_venda_quentinha
	valor_compra_dia1 = num_total_quentinhas_dia1 * preco_compra_quentinha
	valor_lucro_dia1 = valor_venda_dia1 - valor_compra_dia1
	valor_venda_dia2 = num_total_quentinhas_dia2 * preco_venda_quentinha
	valor_compra_dia2 = num_total_quentinhas_dia2 * preco_compra_quentinha
	valor_lucro_dia2 = valor_venda_dia2 - valor_compra_dia2
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
	 "valor_total_compra": valor_total_compra, "valor_total_lucro":valor_total_lucro, "valor_venda_dia1":valor_venda_dia1,
	 "valor_compra_dia1":valor_compra_dia1,"valor_venda_dia2":valor_venda_dia2,"valor_compra_dia2":valor_compra_dia2,
	 "valor_lucro_dia2":valor_lucro_dia2,"valor_lucro_dia1":valor_lucro_dia1,
	 })
