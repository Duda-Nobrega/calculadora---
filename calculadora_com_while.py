while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite um número: ')
    
    numeros_validos = None #flag 

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None
    if numeros_validos is None:
        print('Os números não são válidos')
        continue
   
    operador = input('Escolha um operador: +-/*: ')
    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    if len(operador)>1:
        print('Digite apenas um operador')
        continue
    
    if operador == '+':
        soma = num1_float + num2_float
        print(f'A soma entre {num1_float} e {num2_float} é {soma}')
    elif operador == '-':
        sub = num1_float - num2_float
        print(f'A subtração entre {num1_float} e {num2_float} é {sub}')
    elif operador == '*':
        mult = num1_float * num2_float
        print(f'A multiplicação entre {num1_float} e {num2_float} é {mult}')
    elif operador == '/':
        if num2_float == 0:
            print("Não é possível realizar uma divisão por 0")
            continue
        else:
            div = num1_float/num2_float
            print(f'A divisão de {num1_float} por {num2_float} é {div}')

    sair = input('Deseja sair? [s]air ').lower().startswith('s')
    if sair:
        break
    else:
        continue
