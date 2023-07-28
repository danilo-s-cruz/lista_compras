'''
FUNÇÕES - LISTA DE COMPRAS
'''
def adicionar_produto(lista_produtos):
    nome = input('Digite o nome do produto: ').upper().strip()
    quantidade = int(input('Digite a quantidade do produto: '))
    valor_unitario = float(input('Digite o valor unitário do produto: '))
    total_produto = quantidade * valor_unitario

    produto = {
        'nome': nome,
        'valor': valor_unitario,
        'quantidade': quantidade,
        'total_produto': total_produto
    }

    lista_produtos.append(produto)
    print('Produto adicionado com sucesso!')
    print('Valor total do produto:', total_produto)

def listar_produtos(lista_produtos):
    if lista_produtos == []:
        print('Lista de Compras sem produtos cadastrados.') 
    else:
        print('Lista de produtos:')
        print('------------------------')
        for produto in lista_produtos:
            print('Nome:', produto['nome'])
            print('Valor unitário:', produto['valor'])
            print('Quantidade:', produto['quantidade'])
            print('Valor total:', produto['total_produto'])
            print('------------------------')
        print('Valor total de todos os produtos:', calcular_valor_total(lista_produtos))

def atualizar_produto(lista_produtos):
    if lista_produtos == []:
        print('Lista de Compras vazia.') 
    else:
        nome_produto = input('Digite o nome do produto que deseja atualizar: ').upper().strip()
        for produto in lista_produtos:
            if produto['nome'] == nome_produto:
                print('Produto encontrado!')
                print('Digite as novas informações do produto:')
                nome = input('Nome: ').upper().strip()
                quantidade = int(input('Quantidade: '))
                valor_unitario = float(input('Valor unitário: '))

                produto['nome'] = nome
                produto['quantidade'] = quantidade
                produto['valor'] = valor_unitario
                produto['total_produto'] = quantidade * valor_unitario

                print('Produto atualizado com sucesso!')
                print('Valor total do produto:', produto['total_produto'])
                return
        print('Produto não encontrado na lista!')

def remover_produto(lista_produtos):
    if lista_produtos == []:
        print('Lista de Compras vazia.') 
    else:
        nome_produto = input('Digite o nome do produto que deseja remover: ').upper().strip()
        for produto in lista_produtos:
            if produto['nome'] == nome_produto:
                lista_produtos.remove(produto)
                print('Produto removido com sucesso!')
                print('Valor total de todos os produtos:', calcular_valor_total(lista_produtos))
                return
        print('Produto não encontrado na lista!')

def calcular_valor_total(lista_produtos):
    valor_total = 0
    for produto in lista_produtos:
        valor_total += produto['total_produto']
    return valor_total

def exibir_menu():
    print('-------------------------')
    print('* LISTA DE COMPRAS V1.0 *')
    print('--------- MENU ----------')
    print('  1. Adicionar Produto' )
    print('  2. Listar Produtos' )
    print('  3. Atualizar Produto' )
    print('  4. Remover Produto' )
    print('  5. Encerrar programa' )
    print('-------------------------')