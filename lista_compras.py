'''
LISTA DE COMPRAS
'''
from func_lista_compras import *

def main():
    lista_produtos = []
    while True:
        exibir_menu()
        try:
            opcao = int(input('Digite uma opção (1-5): '))
        except ValueError:
            print('Ops! Escolha uma opção entre 1 e 5.')
            continue

        if opcao == 1:
            adicionar_produto(lista_produtos)
        elif opcao == 2:
            listar_produtos(lista_produtos)
        elif opcao == 3:
            atualizar_produto(lista_produtos)
        elif opcao == 4:
            remover_produto(lista_produtos)
        elif opcao == 5:
            print('Encerrando... Volte sempre!')
            break
        else:
            print('Ops! Escolha uma opção entre 1 e 5.')

if __name__ == '__main__':
    main()