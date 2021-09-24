class cliente:
    nome = None
    cpf = None
    email = None
    senha = None
    limiteCredito = 1000
    carrinho = []


class produto:
    def __init__(self, nome, valor, estoque):
        self.nome = nome
        self.valor = valor
        self.estoque = estoque


# Criando os produtos
def criaProdutos():
    titulos = ["Atlas", "Percy Jefferson", "Probability and Computing", "Lord of the Things", "Dom Pixote",
               "A Song of Ice and Cream", "Modern Operating Systems", "Harry Pote",
               "Guia: como ser bonito como o Guilherme",
               "Dom Casmorro", "JoJo's Bizarre Avenue", "Hunger Plays", "O Corniço", "The Chalk Bro",
               "Guia: como ser esbelto como o Andrei",
               "Software Engineering", "The Chronicles of Naria", "Twilighter", "Hunt x Hunt", "Os Certões"]

    precos = [30.00, 50.00, 200.00, 45.00, 20.00,
              25.00, 350.00, 50.00, 100.00, 30.00,
              930.00, 55.00, 15.00, 60.00, 100.00,
              170.00, 40.00, 45.00, 30.00, 35.00]

    quant = [25, 10, 3, 15, 20, 10, 3,
             10, 2, 22, 1, 7, 30, 20,
             2, 5, 11, 9, 20, 25, ]

    produtos = []

    # Adicionar os podutos à lista:
    for i in range(20):
        produtos.append(produto(titulos[i], precos[i], quant[i]))

    return produtos

#Criando a lista produtos com a função criaProdutos()
produtos= criaProdutos()

#Lista em que os clientes cadastrados ficam salvos
clientes = []

clienteAtualIndex = int()

# Adicionar mais crédito
def adicionar_credito(cliente):
    cartao = str(input("Digite o número do cartão de crédito: "))
    anoVencimento = int(input("Digite o ano de vencimento: "))
    titular = str(input("Digite o nome do titular do cartão: "))
    add = float(input("Digite a quantidade de crédito que deseja adicionar: "))
    cliente.limiteCredito += add


# Pagar conta
def pagar_conta(valor_conta, clienteAtual):
    if valor_conta <= clienteAtual.limiteCredito:
        print(f"Crédito atual: {clienteAtual.limiteCredito}")
        print(f"Valor à ser pago: {valor_conta}")
        print("""
        [1] Concluir Compra
        [2] Esvaziar carrinho
        [3] Retornar ao menu
        """)
        opt = int(input("Digite a opção que deseja selecionar: "))

        if opt == 1:
            #Imprime o carrinho
            clienteAtual.limiteCredito -= valor_conta
            print(10 * "-=", "COMPRA CONCLUIDA", 10 * "=-")
            print(3 * "-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Produtos adquiridos:")
            print(f"{'Produtos' : <40}{'Quantidade' : ^16}{'Preço' :>15}")
            for b in clienteAtual.carrinho:
                print(f"{b[0] : <40}{b[1] : ^16}{b[2] :>15}")
            print(f"{'Total' :<40}{valor_conta :>31}")
            print(3 * "-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

            #Zera o carrinho e o valor à ser pago
            clienteAtual.carrinho = []
            valor_conta = 0


        elif opt == 2:
            #Adiciona novamente os produtos ao seus devidos estoques
            for i in produtos:
                for j in clienteAtual.carrinho:
                    if j[0] == i.nome:
                        i.estoque += j[1]

            #Zera o carrinho e o valor à ser pago
            clienteAtual.carrinho = []
            valor_conta = 0
            print(10 * "-=", "CARRINHO ESVAZIADO", 10 * "=-")

        elif opt == 3:
            pass
        else:
            print("Opção Inválida")
            print()

    #Essa parte do código só é chamada caso o valor á ser pago seja maior que o crédito
    else:
        print(f"Crédito atual: {clienteAtual.limiteCredito}")
        print(f"Valor à ser pago: {valor_conta}")
        print("""Seu saldo atual não é o suficiente
        [1]Esvaziar o Carrinho
        [2]Adicionar Crédito
        [3]Retornar ao Menu
        """)

        opt = int(input("Digite a opção que deseja selecionar: "))

        if opt == 1:

            #Adiciona novamente os produtos ao seus devidos estoques
            for i in produtos:
                for j in clienteAtual.carrinho:
                    if j[0] == i.nome:
                        i.estoque += j[1]

            #Zera o carrinho e o valor a ser pago
            clienteAtual.carrinho = []
            valor_conta = 0
            print(10 * "-=", "CARRINHO ESVAZIADO", 10 * "=-")
        elif opt == 2:
            adicionar_credito(clienteAtual)
        elif opt == 3:
            pass
        else:
            print("Opção Inválida")
            print()

    #Retorna o novo valor da conta(ou zero, ou o mesmo)
    return valor_conta


# Validação do CPF
def validCpf(cpf):
    validation = True
    var = 0

    # Verifica se o CPF já foi registrado
    for i in clientes:
        if i.cpf == cpf:
            validation = False

    # Verifica se o CPF é válido
    if validation:
        if len(cpf) == 11:
            var += int(cpf[8]) * 2
            var += int(cpf[7]) * 3
            var += int(cpf[6]) * 4
            var += int(cpf[5]) * 5
            var += int(cpf[4]) * 6
            var += int(cpf[3]) * 7
            var += int(cpf[2]) * 8
            var += int(cpf[1]) * 9
            var += int(cpf[0]) * 10

            verification1 = var % 11

            if verification1 < 2:
                verification1 = 0
            else:
                verification1 = 11 - verification1

            var = 0
            var += int(cpf[9]) * 2
            var += int(cpf[8]) * 3
            var += int(cpf[7]) * 4
            var += int(cpf[6]) * 5
            var += int(cpf[5]) * 6
            var += int(cpf[4]) * 7
            var += int(cpf[3]) * 8
            var += int(cpf[2]) * 9
            var += int(cpf[1]) * 10
            var += int(cpf[0]) * 11

            verification2 = var % 11

            if verification2 < 2:
                verification2 = 0
            else:
                verification2 = 11 - verification2

            if int(cpf[9]) == verification1 and int(cpf[10]) == verification2:
                validation = True
            else:
                validation = False

        else:
            validation = False

    return validation


# Cadastro de clientes
def cadastro(clientes):
    clienteTemp = cliente()
    clienteTemp.nome = str(input("Digite Seu Nome: "))

    # Registra e valida o CPF
    while True:
        clienteTemp.cpf = str(input("Digite Seu CPF:"))
        if validCpf(clienteTemp.cpf):
            break
        else:
            print("CPF inválido ou já em uso, tente novamente")

    # Registra e valida o email
    while True:
        clienteTemp.email = str(input("Digite o Seu Email: "))
        if clienteTemp.email.find("@") != -1:
            break
        else:
            print("Email inválido, tente novamente")

    # Registra e valida a senha(checa se tem 6 caracteres)
    while True:
        validPass = True
        clienteTemp.senha = str(input("Digite Sua Senha: "))

        for i in clientes:
            if i.senha == clienteTemp.senha:
                validPass = False

        if validPass:
            if len(clienteTemp.senha) == 6 and clienteTemp.senha.isdecimal():
                break
            else:
                print("A senha deve ter 6 digitos, tente novamente")
        else:
            print("Senha já em uso. Escolha Outra.")

    print()
    print("------CADASTRO COMPLETO-------")
    print()

    clienteTemp.limiteCredito = 1000
    clienteTemp.carrinho = []

    clientes.append(clienteTemp)


# Login para entrar no sistema
def login(clientes):
    validation = False

    cpfTemp = str(input("Digite seu CPF: "))

    senhaTemp = str(input("Digite sua Senha: "))

    for i in range(len(clientes)):
        # Valida o login e indica o índice do cliente em clienteAtualIndex
        if clientes[i].cpf == cpfTemp and senhaTemp == clientes[i].senha:
            validation = True
            global clienteAtualIndex
            clienteAtualIndex = i

    return validation

#Menu de compras e carrinho
def compras(clienteAtual):
    # Checa se há elementos em carrinho, caso hajam, o preço de cada elemento é adicionado
    preco = 0
    if clienteAtual.carrinho != []:
        for i in clienteAtual.carrinho:
            preco += i[2]

    # Mostra a lista de produtos
    numero = 0
    print(3 * "-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Lista de Produtos:")
    print("")
    print(f"{'Opção' : <10}{'Nome' : ^40}{'Preço' : ^10}{'Em estoque' :^15}")
    for a in produtos:
        print(f"{numero : <10}{a.nome : ^40}{a.valor :^10}{a.estoque :^15}")
        numero += 1
    print(3 * "-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    # Loop para o menu "compras e carrinho"
    while True:
        selecionada = int(input(
            "Para comprar algo, digite o número da opção. Caso deseje acessar o carrinho, digite 20; Caso queira voltar ao menu, digite -1: "))
        if selecionada > 20 or selecionada < -1:
            print("Opção inválida.")

            continue
        # Carrinho
        elif selecionada == 20:
            print(3 * "-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Seu carrinho:")
            print(f"{'Produtos' : <40}{'Quantidade' : ^16}{'Preço' :>15}")
            for b in clienteAtual.carrinho:
                print(f"{b[0] : <40}{b[1] : ^16}{b[2] :>15}")
            print(f"{'Total' :<40}{preco :>31}")
            print(3 * "-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        elif selecionada < 20 and selecionada >= 0:
            quantia = (int(input(f"Quantidade de {produtos[selecionada].nome} que deseja comprar: ")))
            if quantia < 1:
                print("Quantidade inválida.")

            else:
                # Teste de estoque
                if quantia > produtos[selecionada].estoque:
                    print(f"Estoque indisponível. Estoque máximo: {produtos[selecionada].estoque}")

                elif quantia <= produtos[selecionada].estoque:
                    if preco + produtos[selecionada].valor * quantia > clientes[clienteAtualIndex].limiteCredito:
                        print("Você não tem saldo para isso. Pague os produtos atuais e libere mais saldo")

                    else:
                        print(
                            f"{quantia} unidades de {produtos[selecionada].nome} adicionadas ao carrinho. Valor total: R$ {produtos[selecionada].valor * quantia:.2f}")
                        produtos[selecionada].estoque -= quantia
                        clienteAtual.carrinho.append([produtos[selecionada].nome, quantia, produtos[selecionada].valor * quantia])
                        preco += produtos[selecionada].valor * quantia


        # Sair do menu
        elif selecionada == -1:
            break

    return preco


# Menu após o login concluído
def loginMenu():

    #Checa se existem elementos no carrinho, se existirem, o preço é adicionado ao valor a ser pago
    #A variável valor_conta é a que vai ser descontada do credito no final da compra
    valor_conta = 0
    if clientes[clienteAtualIndex].carrinho != []:
        for i in clientes[clienteAtualIndex].carrinho:
            valor_conta += i[2]

    while True:

        print(20 * "-=")
        print(f"Seja Bem Vindo {clientes[clienteAtualIndex].nome}")
        print(f"Seu saldo atual é {clientes[clienteAtualIndex].limiteCredito}")
        print("-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("1[Fazer Compras & Ver Carrinho]")
        print("2[Pagar conta]")
        print("3[Adicionar Crédito]")
        print("4[Sair para a pagina de login e cadastro]")
        print("-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        opt = int(input("Digite a opção que deseja selecionar: "))

        if opt == 1:
            valor_conta = compras(clientes[clienteAtualIndex])

        elif opt == 2:
            if valor_conta != 0:
                valor_conta = pagar_conta(valor_conta, clientes[clienteAtualIndex])
            else:
                print("Nenhum item adicionado ao carrinho")

        elif opt == 3:
            adicionar_credito(clientes[clienteAtualIndex])

        elif opt == 4:
            break

        else:
            print("Opção Inválida, Tente Novamente")


# Menu de cadastro e login
def menu():
    while True:
        print("Escolha a opção que deseja selecionar ")
        print("""
            [1]Cadastro
            [2]Login
            [3]Desligar""")
        print()

        opt1 = int(input(""))

        if opt1 == 1:
            cadastro(clientes)


        elif opt1 == 2:
            validLogin = False
            while True:
                if login(clientes):
                    validLogin = True
                    break
                else:
                    print("CPF ou senha incorretos. Digite [N] para sair ou qualquer tecla para continuar")
                    resp = str(input())
                    if resp.upper() == "N":
                        break
            if validLogin:
                loginMenu()

        elif opt1 == 3:
            break

        else:
            print("Opção Inválida, Tente Novamente")


menu()