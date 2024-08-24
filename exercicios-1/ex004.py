# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input("Digite algo: ")

print('O tipo primitivo desse valor é:',type(a))
print('Só tem espaços: ', a.isspace())
print('É um numero?', a.isalnum())
print('É alphabeto? ',a.isalpha())
print('É alphanumerico?', a.isalnum())