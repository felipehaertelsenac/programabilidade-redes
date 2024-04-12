print("Dados dos ALunos cadastrados em notas.txt")
print("-----------------------------------------")
numA = 0
numR = 0
arq = open("notas.txt", "r")
linha = arq.readline()
while linha != "":
    partes = linha.split(";")
    print(partes[0] + " - " + partes[1])
    nota = float(partes[1])
    if nota >= 7:
        numA = numA + 1
    else:
        numR = numR + 1
    linha = arq.readline()
arq.close()
print("-----------------------------------------")
print("Aprovados.: ", numA)
print("Reprovados: ", numR)