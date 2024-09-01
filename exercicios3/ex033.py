# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo  número: "))
num3 = int(input("Terceiro número: "))

# VERIFICAÇÃO DO MENOR 
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

# VERIFICAÇÃO DO MAIOR
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f"O menor valor digitado foi {menor}")
print(f"O maior valoe digitador foi {maior}")