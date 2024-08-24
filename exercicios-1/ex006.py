# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input("Informe um numero: "))

dobro = num * 2
trip  = num * 3
r_quad = num ** (1/2)

print(f'O dobro de {num} é: {dobro}\nO triplo de {num} é:{trip}.\nA raiz quadrada de {num} é: {r_quad}')