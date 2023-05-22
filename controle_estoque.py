# ---------------- Variáveis Globais ----------------
listaPeca = []
codigoPeca = 0


# ---------------- Fim das Variáveis Globais ----------------

# ---------------- Início do cadastrarPeca(codigo) ----------------
def cadastrarPeca(codigo):
    print("Você Selecionou a Opção de Cadastrar Peças")
    print(f"Código da Peça 00{codigo}")
    nome = input("Por favor entre com o NOME da Peça: ")
    fabricante = input("Por favor entre com o FABRICANTE da Peça: ")
    valor = int(input("Por favor entre com o VALOR(R$) da Peça: "))
    dicionario_peca = {"codigo": codigo,
                       "nome": nome,
                       "fabricante": fabricante,
                       "valor": valor}
    listaPeca.append(dicionario_peca.copy())
    # ---------------- Fim do cadastrarPeca(codigo) ----------------


# ---------------- Início do consultarPeca() ----------------
def consultarPeca():
    print("Você Selecionou a Opção de Consultar Peça")
    while True:
        opcao_consultar = input("Escolha a opção deseja:\n"
                                "1-Consultar todas as Peças\n"
                                "2-Consultar Peças por Código\n"
                                "3-Consultar Peças por Fabricante\n"
                                "4-Retornar\n"
                                ">> ")
        if opcao_consultar == "1":
            # Peça irá varrer toda a lista de peças
            for peca in listaPeca:
                print("------------------------")
                # Irá varrer todos os conjuntos chaves e valor do dicionário peça
                for key, value in peca.items():
                    print(f"{key}: {value}")
                print("------------------------")

        elif opcao_consultar == "2":
            print("Você Selecionou a Opção de Consultar Peças por Código")
            valor_desejado = int(input("Digite o CÓDIGO da Peça: "))
            for peca in listaPeca:
                # O valor do campo código desse dicionário é igual o valor desejado
                if peca["codigo"] == valor_desejado:
                    print("------------------------")
                    for key, value in peca.items():
                        print(f"{key}: {value}")
                    print("------------------------")

        elif opcao_consultar == "3":
            print("Você Selecionou a Opção de Consultar Peças por Fabricante")
            valor_desejado = input("Digite o FABRICANTE da Peça: ")
            for peca in listaPeca:
                # O valor do campo código desse dicionário é igual o valor desejado
                if peca["fabricante"] == valor_desejado:
                    print("------------------------")
                    for key, value in peca.items():
                        print(f"{key}: {value}")
                    print("------------------------")

        elif opcao_consultar == "4":
            # Saí da função consultar_produto e volta para o Main
            return
        else:
            print("Opção Inválida. Tente novamente: ")
            # Volta para o começo do "while True"
            continue

    # ---------------- Fim do consultarPeca() ----------------


# ---------------- Início do removerPeca() ----------------
def removerPeca():
    print("Você Selecionou a Opção de Remover Peça")
    valor_desejado = int(input("Digite o código da peça a ser removida: "))
    for peca in listaPeca:
        if peca["codigo"] == valor_desejado:
            listaPeca.remove(peca)
    # ---------------- Fim de removerPeca() ----------------


# ---------------- Início do Main ----------------
print("Bem Vindo ao Controle de Estoque de Bicletaria do Lucas lima de Ávila")
while True:
    opcao_principal = input("Escolha a opção deseja:\n"
                            "1-Cadastar Peças\n"
                            "2-Consultar Peças\n"
                            "3-Remover Peças\n"
                            "4-Sair\n"
                            ">> ")
    if opcao_principal == "1":
        codigoPeca += 1
        cadastrarPeca(codigoPeca)
    elif opcao_principal == "2":
        consultarPeca()
    elif opcao_principal == "3":
        removerPeca()
    elif opcao_principal == "4":
        # Encerra o "while True" e o programa encerra
        break
    else:
        print("Opção Inválida. Tente novamente: ")
        # Volta para o começo do "while True"
        continue
# ---------------- Fim do Main ----------------
