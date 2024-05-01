import random

opciones = ('piedra', 'papel', 'tijera')

user_wins = 0
pc_wins =  0

rounds = 1

while True:

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    user_option = input("Piedra, papel o tijera: ")
    user_option = user_option.lower()
    computer_option = random.choice(opciones)

    print('El usuario eligio: ', user_option)
    print('La computadora eligio: ',computer_option)

    if user_option == computer_option:
        print("Empate!")

    elif (user_option == 'tijera' and computer_option == 'piedra')\
        or (user_option == 'piedra' and computer_option == 'papel')\
        or (user_option == 'papel' and computer_option == 'tijera'):
            print('perdiste!, suerte para la proxima')
            pc_wins += 1

    elif (user_option == 'tijera' and computer_option == 'papel')\
        or (user_option == 'piedra' and computer_option == 'tijera')\
        or (user_option == 'papel' and computer_option == 'piedra'):
            print('ganaste!, felicidades!')
            user_wins +=1

    else:
        print('Escribe una opcion valida por favor.')
    
    print('Marcador : ', 'Usuario =>', user_wins, 'PC wins =>', pc_wins)

    if user_wins == 3:
        print('GANASTE EL JUEGO')
        print('Marcador final :',\
            'Usuario: ', user_wins, \
                'PC Wins :', pc_wins)
        break
    if pc_wins == 3:
        print('PERDISTE EL JUEGO')
    
        print('Marcador final :',\
            'Usuario: ', user_wins, \
                'PC Wins :', pc_wins)
        break
    rounds +=1
