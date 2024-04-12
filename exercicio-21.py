valor_1 = float(input('digite o primeiro valor: '))

while True:
    valor_2 = float(input('digite o segundo valor: '))
    
    if valor_2 != 0:
        break
    else:
        print('VALOR INVÁLIDO')

resultado = valor_1 / valor_2
print(resultado)