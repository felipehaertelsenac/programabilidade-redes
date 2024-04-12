import os


def titulo(texto, simbolo='-', quant=40):
    print()
    print(texto)
    print(simbolo*quant)

# Parâmetros posicionais
#titulo('Loja', '=', 50)
# Parâmetros nomeados
#titulo(quant=50, texto="Loja Avenida")


def inclusao():
    titulo('Inclusão de Produtos', '=')

    produto = input('Produto...: ')
    quant = int(input('Quantidade: '))
    preco = float(input('Preço R$..: '))

    # open: nome do arquivo e modo de abertura
    arq = open('produtos.txt', 'a')
    arq.write(f'{produto};{quant};{preco}\n')
    arq.close()

    print('Ok! Produto cadastrado com sucesso!')


def listagem():
    titulo('Listagem de Produtos', '=', 47)

    # se o arquivo não existe
    if not os.path.isfile('produtos.txt'):
        print('Não há produtos cadastrados...')
        return

    arq = open('produtos.txt')          # abre o arquivo para leitura
    linhas = arq.readlines()            # lê todas as linhas em uma lista (array)
    arq.close()                         # fecha o arquivo

    print(f'Nº Produto{"."*23} Quant. Preço R$:')
    print()

    # obtém cada linha da lista de linhas
    for i, linha in enumerate(linhas):
        # divide a linha em partes (lista) a cada ocorrência do ';'
        partes = linha.split(';')
        # partes[0] = "martelo"
        # partes[1] = 3
        # partes[2] = 19.50

        produto = partes[0]
        quant = int(partes[1])
        preco = float(partes[2])

        print(f'{i+1:2d} {produto:30s}  {quant:4d}  {preco:9.2f}')

    print('='*47)


def pesquisa():
    titulo('Pesquisa de Produtos em Estoque', '=')

    palavra = input('Informe a palavra-chave: ')

    arq = open('produtos.txt')          # abre o arquivo para leitura
    linhas = arq.readlines()            # lê todas as linhas em uma lista (array)
    arq.close()                         # fecha o arquivo

    print(f'Produto{"."*23} Quant. Preço R$:')
    print()

    # contador / flag / sinalizador para verificar se existe produto com a palavra-chave informada
    contador = 0

    # obtém cada linha da lista de linhas
    for linha in linhas:
        # divide a linha em partes (lista) a cada ocorrência do ';'
        partes = linha.split(';')

        produto = partes[0]
        quant = int(partes[1])
        preco = float(partes[2])

        if palavra.lower() in produto.lower():
            print(f'{produto:30s}  {quant:4d}  {preco:9.2f}')
            contador = contador + 1

    if contador == 0:
        print('Obs.: * Não há produtos em estoque com a palavra informada')

    print('='*47)


def balanco():
    titulo('Balanço Geral do Estoque', '*', 45)

    arq = open('produtos.txt')          # abre o arquivo para leitura
    linhas = arq.readlines()            # lê todas as linhas em uma lista (array)
    arq.close()                         # fecha o arquivo

    num = len(linhas)
    total = 0

    # obtém cada linha da lista de linhas
    for linha in linhas:
        # divide a linha em partes (lista) a cada ocorrência do ';'
        partes = linha.split(';')

        quant = int(partes[1])
        preco = float(partes[2])

        total = total + (quant * preco)

    print(f'Nº de Produtos em Estoque: {num}')
    print(f'Total em Estoque R$......: {total:9.2f}')


def exclusao():
    listagem()

    num = int(input('Informar o produto a ser excluido (0, para cancelar): '))

    if num == 0:
        return    

    arq = open('produtos.txt')
    linhas = arq.readlines()
    arq.close()

    if num > len(linhas):
        print('Código é invalido')
        return
    
    linhas.pop(num-1)

    arq = open('produtos.txt', 'w')
    arq.write(''.join(linhas))
    arq.close()

    print('Produto excluido!')


while True:
    titulo('Menu Principal - Ferragem Avenida')
    print('1. Inclusão de Produtos')
    print('2. Listagem de Produtos')
    print('3. Pesquisa em Estoque')
    print('4. Balanço Total')
    print('5. Exclusão de Produto')
    print('6. Finalizar')
    opcao = int(input('Opção: '))
    if opcao == 1:
        inclusao()
    elif opcao == 2:
        listagem()
    elif opcao == 3:
        pesquisa()
    elif opcao == 4:
        balanco()
    elif opcao == 5:
        exclusao()
    else:
        break
