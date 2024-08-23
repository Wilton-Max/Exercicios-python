# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input("Informe o salário:" ))

aumento = sal * 15/100
novo_sal = sal + aumento

print(f'O novo salario com o aumento de 15% é: {novo_sal:.2f} R$')