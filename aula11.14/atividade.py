lista = []
lista = [ '40', '80', '10', '70', '30']
print(lista)
lista.remove ('10')
print(lista)

lista_consoante = []
letra_1 = input("digite uma letra") 
letra_2 = input("digite uma letra") 
letra_3 = input("digite uma letra") 
letra_4 = input("digite uma letra") 
letra_5 = input("digite uma letra") 

if letra_1 != 'a' and letra_1 != "e" and letra_1 != 'i' and letra_1 != 'o' and letra_1 != 'u':
    print("é uma consoante!")
    lista_consoante.append(letra_1)