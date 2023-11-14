# alguns cuidados com dados mutaveis
# mutaveis - são dados que podem ter seu valor alterado na memoria do dispositivo.
# imutaveis - são dados que so podem ser copiados da memoria do dispositivo.


nome = 'paulo' 
# nome = 'joão' 
# print(nome)
novo_nome = nome
nome = 'joão'
print(nome)
print(novo_nome)

lista_a = [ 'joão', 'paulo' ]
print(lista_a)
lista_b = lista_a
print(lista_a)
print(lista_b)