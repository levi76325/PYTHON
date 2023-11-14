# CRUD Create.Read.Update.Delete (criar, ler, atualizar e  deletar)
# lista - mutavel, iteravel, suporta varios tipos de dados, possui indices, aceita metodos e fatiamentos.
# OBS.: lista tem seu proprio CRUD
# metodos: append, insert, del, remove, pop, len, extend.
# parametro: []
# listas são um conjunto de elementos
# OBS.: polimorfismos - é a pacacidade de alguma coisa ser utilizada de varias formas em varias situações.

lista_a = [ 1, 2, 3, 4, 5 ]
lista_b = [ 6, 7, 8, 9, 10]

# o sinal de + ele soma numeros e concatena strings

a = 2
b = 3
print(a + b)

c = "Amo"
d =  "Valley"
print( c + d)

lista_c = lista_a + lista_b
print(lista_c, type(lista_c))

lista_a.extend(lista_b)
print(lista_a)
