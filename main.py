from random import choice

#Lista completa del 1 al 9
flat_board = [i for i in range(1, 10)]
board = []


#Lista dividida en 3 partes
for i in range(0, 9, 3):
    board.append(flat_board[i:i+3])


#Asignamos el valor de X del turno del ordenador
num = 5
fila = (num - 1) // 3
columna = (num - 1) % 3

board[fila][columna] = 'X'


#Imprimimos el tablero en orden y centrado
for fila in board:
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|', end='')
    for celda in fila:
        print(f'   {celda}   |', end='')
    print()
    print('|       |       |       |')
print('+-------+-------+-------+')



while True:
    #Preguntamos al usuario que numero de movimiento desea ingresar
    while True:
        try:
            num = int(input('Qué movimiento deseas realizar? '))
            
            if num < 1 or num > 9:
                print('El numero debe de estar entre el 1 y el 9')
                continue    

            fila = (num - 1) // 3
            columna = (num - 1) % 3
        
            if board[fila][columna] == 'X' or board[fila][columna] == 'O':
                print('El numero ya esta ocupado. Elige otro numero')
                continue 

            break

        except ValueError:
            print('Debes ingresar un numero entero valido')

    board[fila][columna] = 'O'

    #Imprimimos el tablero en orden y centrado
    for fila in board:
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print('|', end='')
        for celda in fila:
            print(f'   {celda}   |', end='')
        print()
        print('|       |       |       |')
    print('+-------+-------+-------+')



    #Guardar numeros disponibles
    num_disp = []

    for fila in board:
        for celda in fila:
            if celda != 'X' and celda != 'O':
                num_disp.append(celda)

    #Turno computadora
    num = choice(num_disp)
    fila = (num - 1) // 3
    columna = (num - 1) % 3

    board[fila][columna] = 'X'

    #Imprimimos el tablero en orden y centrado
    for fila in board:
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print('|', end='')
        for celda in fila:
            print(f'   {celda}   |', end='')
        print()
        print('|       |       |       |')
    print('+-------+-------+-------+')

    #break


def victoria():
    #Filas
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] in ['X', 'O']:
        print('Hay un ganador!!!')

    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] in ['X', 'O']:
        print('Hay un ganador!!!')

    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] in ['X', 'O']:
        print('Hay un ganador!!!')


    #Columnas
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] in ['X', 'O']:
        print('Hay un ganador!!!')
    
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] in ['X', 'O']:
        print('Hay un ganador!!!')

    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] in ['X', 'O']:
        print('Hay un ganador!!!')


    #Diagonales
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] in ['X', 'O']:
        print('Hay un ganador!!!')

    elif board[0][0] == board[0][1] == board[0][2] and board[0][0] in ['X', 'O']:
        print('Hay un ganador!!!')

    elif board[0][0] == board[0][1] == board[0][2] and board[0][0] in ['X', 'O']:
        print('Hay un ganador!!!')