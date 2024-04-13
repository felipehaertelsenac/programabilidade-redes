with open("acessos.txt", "r") as arq:
    num = int(arq.readline())

num = num + 1
print(f"Você é o visitante de número: {num}")

with open("acessos.txt", "w") as arq:
    arq.write(str(num))