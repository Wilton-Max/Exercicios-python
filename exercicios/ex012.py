# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Informe o preço do produto: "))

desconto = preco * 5 / 100

valor_final = preco - desconto

print(f'O preço do produto com desconto é: {valor_final} ')