 # Desenvolva um programa que pergunte a distância de uma viagem em Km. 
 # Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Qual a distancia da sua viagem? "))

if distancia <= 200:
    preco = 0.50 * distancia
    print(f"O preço da sua passagem será de: R${preco}")
else:
    preco = 0.45 * distancia
    print(f"O preço da sua passagem é: R${preco}")