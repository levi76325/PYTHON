# for trabalha com iteraveis!!!
# tem que possuir uma variavel de controle
# metodo 
# iter: transforma um objeto em iteravel e o next: função para imprimir os iteraveis de uma "lista".

# enumerate: e um iterador de indices e valores.
'''
nome = 'paulo'
texto = iter(nome)
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

for letra in nome:
    print(letra)
'''

'''
lista_nomes = [ 'Joaõ', 'Pedro', 'Mateus', 'Judas', 'Tiago' ]
lista_enumerada = enumerate(lista_nomes)
print(lista_nomes)
print(list(lista_enumerada))

for item in lista_enumerada:
    print(item)

for item_lista in lista_nomes:
    print(item_lista)

for indice_lista, item_lista in enumerate(lista_nomes):
    print(f'{ item_lista } é o {indice_lista} da lista')
'''
'''
dias_semanas = [ 'domindo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado' ]

for dias in dias_semanas:
    print(dias)
'''

for i in range(0,101):
    print(i)