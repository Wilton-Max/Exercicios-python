
# adição            +
# subtração         -
# multplicação      *
# divisão           /
# potencia         **
# divisão inteira  //
# Resto divisao     %

# ORDEM DE PRECEDENCIA

# 1 -- PARENTESES    ()
# 2 -- EXPONENCIAÇÃO **
# 3 -- MULT * DIV / DIV INTEIRA // RESTO %
# 4 -- MAIS + MENOS - 

## EXEMPLOS DE USO PARA "PRINT"

# print('='*20)
# print('Oi'*7)

n1 = int(input('Infomr um número: '))
n2 = int(input('Informe ou valor: '))

# print('A soma vale {}'.format(n1+n2))
# print(f'A soma vale {n1} + {n2} é {n1+n2}')

soma = n1 + n2
subt = n1 - n2
mult = n1 * n2
div  = n1 / n2
div_inteira = n1 // n2
expon = n1 ** n2

#print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(soma, mult, div))
#print('Divisão inteira {} e potência {}'.format(div_inteira, expon))

print(f'A soma é {soma}, o produto é {mult}, a divisão é {div:.2f}')
print(f'Divisão inteira {div_inteira} e potência {expon}')
