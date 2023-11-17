# Set - conjuntos

set01 = set('levi')
set02 = {'junior', 'felipe', 'lara', 'kaynan', 'paulo'}
print(set02)
print(set01)

lista = [1, 1, 1, 1, 2, 2, 2, 3 ,3 ,3 ,3 ,3 ,4 , 4, 5, 6, 5]
print(lista)
set03 = set(lista)
print(set03)
print(5 in set03)
print(7 in set03)
print(7 not in set03)
print(5 not in set03)

for i in set03:
    print(i)

set03.add('joão')
set03.add(123)
set03.update('paulo')
set03.discard('paulo')
set03.clear()
print(set03)

set4 = {1, 2, 3, 4, 5 }
set5 = {4, 5, 6, 7, 8 }
set6 = set4 | set5 # união de conjuntos
print(set6)

set6 = set4 & set5 # inter de conjuntos
print(set6)

set6 = set4 - set5
print(set6)

set6 = set5 - set4
print(set6)