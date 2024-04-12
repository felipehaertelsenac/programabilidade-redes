macas = int(input('Informe número de maças compradas: '))

if macas < 12:
    valor_total = 0.30 * macas
else:
    valor_total = 0.25 * macas

valor_formatado = "{:.2f}".format(valor_total)
print(f'O valor total da compra é: R$ {valor_formatado}')