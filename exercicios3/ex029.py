 # Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
 # mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input("Informe a velocidade atual do carro: "))

if vel >= 80:
    print("MULTADO! Vocẽ excedeu o limite permitido que é de 80 km/h ")
    excesso = vel - 80
    multa = excesso * 7
    print(f"Você vai pagar uma multa de:{multa}R$")
else:
    print("Tenha um bom dia, pode seguir em frente.")

