# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = input("Escreva o nome do aluno 1: ")
aluno2 = input("Escreva o nome do aluno 2: ")
aluno3 = input("Escreva o nome do aluno 3: ")
aluno4 = input("Escreva o nome do aluno 4: ")

lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print(lista)