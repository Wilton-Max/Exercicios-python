# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit. 

#°F = (°C × 9/5) + 32

c = float(input("Informe a temperatura em celsius:"))
f = (c * 9 / 5) + 32

print(f'O valor de celcius convertios para fahrenheit é: {f}')