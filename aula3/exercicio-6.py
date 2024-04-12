altura = float(input('Informe a sual altura: '))
sexo = input('Informe o seu sexo: (M) Masculino ou (F) Feminino: ')

if sexo == 'm' or sexo == 'M' or sexo == 'Masculino' or sexo == 'masculino':
    peso_ideal = 72.7 * altura - 58
else:
    peso_ideal = 62.1 * altura - 44.7

print(f'O peso ideal é: {peso_ideal}')