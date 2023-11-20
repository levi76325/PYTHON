'''
contador = 0
while contador < 10: 
# enquanto o contador for menor ou igual a 10 faça:
    nota = float(input('iforme uma nota:'))
    if nota <  nota > 10:
        print('sua nota nao foi suficiente para continuar')
        break
    contador = contador + 1
'''
aluno = 1
while aluno <= 20:
    idade = int(input(f'qual idade do aluno{ aluno } ?: '))
    if idade > 13:
        print(f'A idade do aluno { aluno } é { idade }. E maior que 13')
    aluno = aluno + 1
print('Fim da questão!')