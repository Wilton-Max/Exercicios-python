# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc

num = float(input("Informe um número real: "))

num_trunc = trunc(num)

print(num_trunc)