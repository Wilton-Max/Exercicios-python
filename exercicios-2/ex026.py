# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).upper().strip()

frase_a = frase.count('A')
indice = frase.find('A')+1
last = frase.rfind('A')

print(f'A letra A aparece {frase_a} vezes na frase. \nA primeira letra A apareceu na posição {indice}. \nA ultima letra está na posição {last}')