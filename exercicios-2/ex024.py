 
 # Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input("Informe o nome da cidade: ").strip

print(cidade[0:5].upper() == 'SANTO')
