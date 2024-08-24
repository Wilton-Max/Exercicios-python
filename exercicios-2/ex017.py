# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

import math

op  = float(input("Infome o comprimento do cateto oposto: "))
adj = float(input("Informe o comprimento do cateto adjacente: "))


# Usando duas funções do math
''' op =  math.pow(op,2)
    adj = math.pow(adj,2)          
    som = op + adj
    hip = math.sqrt(som)'''

# Usando apenas a função .sqrt
''' hip = op**2 + adj**2
    hip = math.sqrt(hip)'''

#Formula só com matematica sem importação
''' hip = (op**2 + adj**2) ** (1/2)'''

# Formula importanto a função .hypot
hip = math.hypot(op,adj)


print(f'A hipotenusa vai medir {hip:.2f}')