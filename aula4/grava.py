print("Grava dados de Alunos em arquivo texto")

nome = input("Nome: ")
nota = float(input("Nota: "))

arq = open("notas.txt", "a")
if nota >= 7:
    arq.write(nome+";"+str(nota)+";Aprovado\n")
else:
    arq.write(nome+";"+str(nota)+";Reprovado\n")
arq.close()
print("Ok! Dados Cadastrados")