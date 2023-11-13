# list-lista, tuple-tupla, set-conjunto e dictionary-dicionario
# lista-caracteristica: mutavel(iteravel), suporta varios tipos, metodos e fatiamentos,
# e por fim ela tambem possui indices.
# len - metodo que retorna a quantidade de itens de uma lista.
# append - metodo que insere itens no final da lista.
# del - remove item especifico da lista
# remove - ele remove um objeto espefico da lista
itens_compras = ['arroz', 'feijão', 'leite', 'ovos', 'tomate']
for item in itens_compras:
    print(item)
# uma lista é representada pelos []
'''
lista = []
print(lista, type(lista))
print(len(lista))
lista = ['front']
print(lista, type(lista))
print(len(lista))
lista = ['back']
print(lista, type(lista))
print(len(lista))
lista.append('front')
print(lista, type(lista))
print(len(lista))
lista.append('data')
print(lista, type(lista))
print(len(lista))'''
#       0       1       2       3       4
#       -5      -4      -3      -2      -1
lista = [ 'back', 'tarde', 21, True, 8.8 ]
print(f' a quantidade de alunas na turma é: {lista[2]}')
lista[2] = 22
print(lista)
lista[1] = False
print(lista)
lista[1] = ['neyva', 'alice', 'lara', 'paula', 'geisa']
print(lista)

print(lista[-2])
del lista[-2]
print(lista[-2])
lista.remove('back')