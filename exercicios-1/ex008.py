# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input("Informe um valor em metros: "))

# Centmetros = Metros×100

cent = metro * 100
mili = metro * 1000


print(f'{metro} metros são {cent} centrimetros e {mili} milimetros')