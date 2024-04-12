# import datetime # para importar toda a biblioteca
# import datetime as dt # substituindo o nome datetime por dt dentro do código
# from datetime import date # quando se quer apenas 1 dos submódulos

ano_nascimento = int(input('Informe o seu ano de nascimento: '))

idade = 2024 - ano_nascimento

# hoje = datetime.date.today()
# ano_atual = hoje.year
# idade = ano_atual - ano_nascimento

if idade >= 16:
    print('Você pode votar este ano')
else:
    print('Você ainda não pode votar este ano')