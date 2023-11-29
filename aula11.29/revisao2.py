# estruturas condicionais
variavel = 20
if variavel < 20:
    print("menor que 20!!")
elif variavel == 20:
    print("igual a 20!!")
elif variavel > 20 and variavel < 50:
    print("esta no intervalo entre 21 e 49!!")
else:
    print("qualquer outra coisa!!")

# estruturas de repetição
# FOR e WHILE

for i in range(5):
    print(f'numero: {i}')

contador = 5
while contador > 0:
    print(f'Esse é o print do: { contador }')
    contador -= 1

# join = unir strings

lista2 = ['joão', 'paulo', 'II'] 
nome = ' '.join(lista2)
print(nome)
