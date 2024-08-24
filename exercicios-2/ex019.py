# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

aluno1 = input("Escreva o nome do aluno 1: ")
aluno2 = input("Escreva o nome do aluno 2: ")
aluno3 = input("Escreva o nome do aluno 3: ")
aluno4 = input("Escreva o nome do aluno 4: ")

lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = random.choice(lista)

print(f'O aluno sorteado foi: {escolhido}')