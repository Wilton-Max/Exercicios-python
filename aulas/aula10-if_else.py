
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print("Carro novo!")
else:
    print("Carro velho!")
print('---FIM---')

#################################
nome = str(input("Qual seu nome? "))
if nome == 'Gustavo':
    print("Que nome lindo você tem!")
else:
    print("Seu nome é tão normal!")
print(f"Bom dia, {nome}")

#################################
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"A sua media foi:{media}")

if media >= 6:
    print("Parabéns, sua nota foi ótima!")
else:
    print("Sua média foi ruim, ESTUDE MAIS!")