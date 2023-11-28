jogador1 = input('Escolha par ou impar: ').lower()
if jogador1 == 'par':
    jogador2 = 'impar'
else:
    jogador2 = 'par'

numero_jogador1 = int(input('Escolha seu número: '))
numero_jogador2 = int(input('Escolha seu número: '))

resultado = numero_jogador1 + numero_jogador2
if resultado % 2 == 0:
    if jogador1 == 'par':
        print("Jogador 1. Você ganha!!")
    else:
        print("Jogador 2. Você ganha!!")
else:
    if jogador1 == 'impar':
        print("Jogador 1. Você ganha!!")
    else:
        print("Jogador 2. Você ganha!!")