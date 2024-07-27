"""
Faça uma lista de compra com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os

lista_compras = []

while True:

    print('Selecione uma opção')
    entrada = input('[i]nserir [a]pagar [l]istar: ')

    if entrada == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_compras.append(valor)

    if entrada == 'a':
        indice = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice)
            lista_compras.pop(indice)
        except ValueError:
            print('Digite um número inteiro')
        except IndexError:
            print('Esse indice não existe')
            

    if entrada == 'l':
        os.system('cls')

        if lista_compras != []:
            for indice, valor in enumerate(lista_compras):
                print(indice,valor)

        else:
            print('A lista está vazia')