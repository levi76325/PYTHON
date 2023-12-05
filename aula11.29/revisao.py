variavel = 1

print(variavel)

variavel = 'Paulo'

print(variavel)

#fatiamento [inicio, fim, step]
print(variavel[2:4])
print(variavel[::-1])

'''
for i in range(1, 11):
    questão = input(f"Digite a pergunta {i}: ")
    respostas = input(f"Digite a resposta {i} (v ou f): ")
    if respostas == "v":
        respostas = True
    elif respostas == "f":
        respostas = False
    else:
        print("Resposta inválida. Por favor, digite 'v' para verdadeiro ou 'f' para falso.")
        continue
    if respostas == True:
        correta_respostas = True
    else:
     correta_respostas = False
    print(f"Resposta {i}: {respostas}")
    if respostas ==  correta_respostas:
        print("Correto!")
    else:
        print("Incorreto.")
'''

'''
lista = ['a', 'b', 'c', 'd', 'e']
print(lista[0::])

print(lista[0:4])

print(lista[0:3])

print(lista[0:2])

print(lista[0:1])
'''


def fatorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
        print(f"{i}! = {resultado}")
    return resultado

numero = int(input("Digite um número inteiro positivo: "))
fatorial(numero)
