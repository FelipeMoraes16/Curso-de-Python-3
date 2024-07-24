# calculadora

while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-*/): ')

    # flag
    numeros_válidos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_válidos = True

    except:
        numeros_válidos = None

    if numeros_válidos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    operadores_válidos = '+-*/'

    if operador not in operadores_válidos:
        print('Digite um operador válido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    # contas

    print('Resultado abaixo: ')

    if operador == '+':
        print(f'A soma de {num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
    elif operador == '-':
        print(f'A subtração de {num_1_float} - {num_2_float} = ', num_1_float - num_2_float)
    elif operador == '*':
        print(f'A multiplicação de {num_1_float} * {num_2_float} = ', num_1_float * num_2_float)
    elif operador == '/':
        print(f'A divisão de {num_1_float} / {num_2_float} = ', num_1_float / num_2_float)

    print(f'sair')

    sair = input('Quer sair ? [s]im: ').lower().startswith('s')

    if sair:
        break