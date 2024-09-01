 # Escreva um programa que faça o computador “pensar” em um número inteiro entre 
 # 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
 # O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('-=-' * 20)
print("VOU PENSAR EM UM NUMERO DE 0 A 5, TENTE ADVINHAR")
print('-=-' * 20)

jogador = int(input("Em que número eu pensei? "))

print("PROCESSANDO...")

computador = randint(1, 5)

sleep(3)
if jogador == computador:
    print(f"Você venceu, eu escolhi o número{computador}")
else:
    print(f"Você errou, eu escolhi o numero {computador}")