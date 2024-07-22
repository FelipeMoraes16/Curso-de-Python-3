# Exercicio
# Peça ao usuário para digitar seu nome
# Peça ao usuário para digitar sua idade
# Se nome e idade for digitados:
#     Exiba:
#         Seu nome é {nome}
#         Seu nome invertido é {nome invertido}
#         Seu nome contém (ou não) espaços
#         Seu nome tem {n} letras
#         A primeira letra do seu nome é {letra}
#         A última letra do seu nome é {letra}
# Se nada for digitado em nome ou idade:
#     Exiba "Desculpa, você deixou campos vazios."

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome != '' and idade != '':
    if idade.isnumeric():
        idade = int(idade)

        print(f'Seu nome é: {nome}')
        print(f'Seu nome invertido é {nome[::-1]}')
        
        if ' ' in nome:
            print(f'Seu nome contem espaços')
        else:
            print(f'Seu nome não contem espaços')

        print(f'Seu nome tem {len(nome)} letras')
        print(f'A primeira letra do seu nome é {nome[0]}')
        print(f'A última letra do seu nome é {nome[-1]}')

    else:
        print('Desculpe você não digitou um número no campo idade.')
else:
    print('Desculpa, você deixou campos vazios.')