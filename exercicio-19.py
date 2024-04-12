while True:
    nota_1 = float(input('digite a nota da primeira avaliação: '))
    nota_2 = float(input('digite a nota da segunda avaliação: '))

    media_final = (nota_1 + nota_2) / 2
    print(f"A média final foi: {media_final}")

    num = int(input('Calcular a média de outro aluno 1.Sim 2.Não? '))

    if num != 1:
        break