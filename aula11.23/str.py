# count - função é contar quantas vezes um determinado caractere aparece em uma string
# upper e a lower - dois metodos que deixam a string toda em maiscula ou a string minuscula.
# find - busca por uma expressão dentro da frase.
# replace - é utilizado para realizar alterações dentro da string.
# capitalize - deixa a primeira letra das palavras maiusculas.
# split - ele transforma sua string em uma lista.
'''
frase = " A banana é amarela e o abacate e verde. ".lower()

letra = 'a'
print(f' A letra { letra } aparece {frase.count(letra)} vezes na  frase { frase }.')
achei = frase.find('roxo')
if achei >= 0:
    print(f'A expressão foi encontrada no indice { achei }')
else:
    print('A expressão não foi entrada na frase')
saida = input('digite "s" para sair: ').lower()
if saida == 'S':
    print(saida)
'''
'''

nova_frase = frase.replace('banana', 'maracuja')
nova_frase2 = frase.replace('abacate', 'manga')
nova_frase2 = frase.replace(' ', '')
print(frase)
print(nova_frase)
print(nova_frase2)
print(frase.capitalize())
print(frase.split())
'''

'''
leia = input("digite a string: ")
print(leia)
print(len(leia))

nome = input('digite o nome: ')
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
'''

'''
nome2 = input("digite uma string: ")
nome3 = input("digite uma string: ")
if nome2 == nome3:
    print("as duas strings são iguais")
else:
    print("as duas strings são diferentes")
'''

'''
nome = input('digite o nome: ')
vogais = 'aeiou' 
print(f'o nome { nome } tem {nome.count("a,e,i,o,u")} vogais')
'''

'''
nome = input("Informe o nome de usuario: ")
'''

nome = input("Infome a palavra: ") 
print(nome[::-1])