nota_1 = float(input('digite a nota da primeira avaliação: '))
nota_2 = float(input('digite a nota da primeira avaliação: '))

media_final = (nota_1 + nota_2) / 2

if media_final >= 6:
    print('APROVADO')
elif media_final >= 3 :
    print('EXAME')
else:
    print('REPROVADO')