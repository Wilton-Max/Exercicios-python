# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
# quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura  = float(input("Qual a largura da parede?" ))
largura = float(input("Qual a altura da parede?" ))

area = altura * largura

l_tinta = area / 2

print(f'A area da parede é {area}, e são necessários {l_tinta} de tinta para pinta-la')