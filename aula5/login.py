print("Controle de Acessos")

tentativas = 0

while True:
    login = input("Login: ")
    senha = input("Senha: ")

    try:
        with open('usuarios.txt', 'r') as arq:
            linha = arq.readline()
            encontrou = 0

            while linha != "":
                partes = linha.split(";")
                
                if login == partes[0] and senha == partes[1][:-1]:
                    encontrou = 1
                    break

                linha = arq.readline()
    except FileNotFoundError:
        print("Arquivo não encontrado.")

    if not encontrou:
        tentativas = tentativas + 1

        print(f"Erro... inválido - {tentativas}ª tentativa.")
        
        if tentativas == 3:
            print("Limite de tentativas esgotado")
            break
    else:
        print("Acesso Liberado!")
        break  
