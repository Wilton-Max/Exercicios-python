#  Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input("Infome seu nome: ")).strip()
#silva = 'silva' in nome.lower

print(f'Seu nome tem silva: {'silva' in nome.lower()}')