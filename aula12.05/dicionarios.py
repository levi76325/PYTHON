# dicionario = é uma coleção de itens que possuem chave e valor
# inicialização = dic = {} ou dic = dict(chave=valor)
# possui CHAVE(KEYS) e VALOR(VALUES)
# parametro: {} ou dict().
# clear = limpa o dicionario.
# del = exclue uma chave (del.dic[chave]).
# keys = ele vai entregar todas as chaves no dicionario.
# values = ele vai entragar todos os valores.
# items = ele entrega todos os itens com chave e valor. 
# get = ele entraga um valor referenciado pela chave.
# update = ele e utilizado para inserir itens no dicionario
# copy = ele faz uma copia do dicionario garantindo um novo endenreço de memoria.
# sorted = ele ordena um dicionario pelas suas chaves.



pessoa = {  'nome': 'paulo', 
            'sobrenome': 'junior' }

print(len(pessoa))

for chave, valor in pessoa.items():
    print(chave, valor)


d1 = { 'valor': 100,
      'valor2': 200,
      'valor3': 300, }


d2 = d1 

print(d1)

d2['valor2'] = 2000

print(d1)

d3 = d1.pop()

print(d1)
