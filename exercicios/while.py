# iterarando strings com while

nome = 'Felipe Moraes'

indice = 0
tamanho_nome = len(nome)
novo_nome = ''

while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)