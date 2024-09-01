# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. 
# 3 + 4 > 5 (Verdadeiro)
# 3 + 5 > 4 (Verdadeiro)
# 4 + 5 > 3 (Verdadeiro)

print("-="*20)
print("Analizador de triangulo")
print("-="*20)
seg1 = float(input("Infome o primeiro segmento: "))
seg2 = float(input("Infome o segundo  segmento: "))
seg3 = float(input("Infome o terceiro segmento: "))

if (seg1 + seg2) > seg3:
    print("Os segmentos acima podem formar um triangulo.")
else:
    print("Os segmentos acima não podem formar um triangulo.")