#  while = enquanto


# loop infinito
#while True:

contador = 0
while contador < 30:
    print(contador)
    contador += 1 # contador = contador + 1
    print("saiu do while")
    if contador == 12:
        print("cheguei no 12")

    if contador == 290:
        break