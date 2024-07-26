"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'ovo'
letras_acertadas = ''
tentativas = 0

while True:

    letra = input('Digite uma letra: ')
    tentativas += 1

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formatada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formatada += letra_secreta

        else:
            palavra_formatada += '*'

    print('palavra formatada: ', palavra_formatada)

    if palavra_formatada == palavra_secreta:
        os.system('cls')
        print('VOCE GANHOU!')
        print('A palavra secreta era: ',palavra_secreta)
        print('Número de tentativas: ',tentativas)
        letras_acertadas = ''
        tentativas = 0