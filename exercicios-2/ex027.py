# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input("Digite seu nome completo: ")).strip()

nome = n.split()

print(f'O primeiro nome é:{nome[0]}')
print(f'O ultimo nome é: {nome[len(nome)-1]}')

