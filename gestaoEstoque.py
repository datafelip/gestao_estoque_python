import random
estoque = []

def menu():
    try:
        escolha = int(input("1 - Cadastrar Produto\n2 - Listar produtos\n3 - Remover produto\n4 - Atualizar o estoque\n5 - Sair\nDigite aqui o que deseja fazer -->: "))
        if escolha in range(1, 6):
            return escolha
        else:
            print("Opção inválida! Digite um número de 1 a 5.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")
def cadastrarProduto(code, name, stock):
    estoque.append([code, name, stock])
    print(f"O produto {name} foi cadastrado com sucesso!")
def listarProdutos():
    if estoque:
        print("código----produto----estoque")
        for item in estoque:
            print(f"{item[0]:<10} {item[1]:<10} {item[2]}")
    else:
        print("Nenhum produto cadastrado.")
def removerProduto(codigo):
    for item in estoque:
        if codigo == item[0]:
            estoque.remove(item)
            print(f"O produto {item[1]} foi removido com sucesso!")
            return
    print(f"Produto de código {codigo} não está cadastrado.")
def atualizarEstoque(codigo, quantidadeNova):
    for item in estoque:
        if codigo == item[0]:
            item[2] = quantidadeNova
            print(f"A quantidade do produto {item[1]} foi atualizada para {quantidadeNova} unidades")
            return
    print(f"O produto com código {codigo} não está cadastrado.")
while True:
    escolha = menu()
    match escolha:
        case 1:
            while True:
                codigoProduto = random.randint(1, 3000)
                if not any(item[0] == codigoProduto for item in estoque):
                    break
            nomeProduto = str(input("Digite o nome do produto que deseja cadastrar: ")).lower().strip()
            if not nomeProduto:
                print("O campo não pode estar vazio.")
            else:
                while True:
                    try:
                        quantidadeEstoque = int(input(f"Digite a quantidade de {nomeProduto} no estoque: "))
                        if quantidadeEstoque >= 0:
                            cadastrarProduto(codigoProduto, nomeProduto, quantidadeEstoque)
                            listarProdutos()
                            break
                        else:
                            print("A quantidade deve ser positiva!")
                    except ValueError:
                        print("Digite um número válido para quantidade.")
        case 2:
            listarProdutos()
        case 3:
            listarProdutos()
            excluirItem = int(input("Digite o código do produto que deseja retirar: "))
            if excluirItem:
                removerProduto(excluirItem)
            else:
                print("O campo não pode estar vazio.")
        case 4:
            if estoque:
                listarProdutos()
                codigoProduto = int(input("Digite o código do produto que deseja atualizar o estoque: "))
                if codigoProduto:
                    try:
                        quantidadeAtualizar = int(input("Digite para quanto deseja atualizar: "))
                        if quantidadeAtualizar > 0:
                            atualizarEstoque(codigoProduto, quantidadeAtualizar)
                        else:
                            print("A quantidade deve ser positiva.")
                    except ValueError:
                        print("Digite um número válido para quantidade!")
                else:
                    print('O campo não pode estar vazio.')
            else:
                print("Nenhum produto cadastrado.")

        case 5:
            sair = str(input("Deseja sair?\nDigite 's' para sim e 'n' para não\nDigite aqui -->: ")).lower()
            if sair == "s":
                print("Até a próxima:)")
                break
            elif sair != "n":
                print("Opção inválida, retornando ao menu principal.")
            else:
                print("OK! Retornando.")