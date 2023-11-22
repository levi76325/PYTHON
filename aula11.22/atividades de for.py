# 1º - faça um programa que peça 10 numeros inteiros, calcule 
#e mostre a quantidade de numeros inpares e a quantidade de numeros pares

# 10 repetições
'''

contador_par = 0
contador_inpar = 0
for i in range(1, 11):
    numero = int(input(f'Informe o { i } numero: '))
    if numero % 2 ==  0:
        contador_par += 1
    else:
        contador_inpar += 1

print(f'A quantidade de numeros pares é { contador_par }')
print(f'A quantidade de numeros inpares é { contador_inpar }')
'''

# 2º - faça um programa que, dado um conjunto de n numeros, determine o menor valor, 
# #o maior valor e a soma dos valores

'''
maior = 0 
menor = None
while True:
    saida = input('digite S para sair: ')
    if saida == 's' or saida == 'S':
        print('Volte sempre!!!')
        break

    numero = int(input('Informe um numero inteiro: '))

    if numero > maior:
        maior = numero

    if menor == None or numero < menor:
        menor = numero

print(f'A soma de { maior } + { menor } = {maior+menor}')
print(f'O maior valor é: { maior }')
print(f'O menor valor é: { menor }')
'''

'''
# 3º - Faça um programa que peça um numero inteiro e determine se ele é ou não um 
# #numero primo. Um numero primo é aquele que e divisivel somente por ele mesmo e por 1.

numero = int(input('Informe um numero inteiro: '))
intervalo = range(1, numero+1)
contador = 0 
for i in intervalo:
    if numero % i == 0:
        print(f'Foi divisivel por { i }')
    contador += 1

if contador == 2:
    print(f'O numero { numero } é primo: ')

'''
