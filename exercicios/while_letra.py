# Qual letra aparece mais

frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma, ' \
    'Python foi criado por Guido van Rossum.'

indice = 0
tamanho_frase = len(frase)
letra_final = ''
quantidade_final = 0
letra_atual = ''
quantidade_atual = 0

while indice < tamanho_frase:

    if frase[indice] == ' ':
        indice += 1
        continue

    letra_atual = frase[indice]
    quantidade_atual = frase.count(letra_atual)

    if quantidade_final < quantidade_atual:
        letra_final = letra_atual
        quantidade_final = quantidade_atual

    indice += 1

print(
    f'A letra que mais apareceu foi "{letra_final}", '\
    f'e ela apareceu {quantidade_final}x'
)