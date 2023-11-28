# funções são blocos de codigos que são executados somente quando são chamados.
# parametro: def
# OBS: as funções devem ter prioridade no codigo.
def media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media 
nota1 = int(input('Informe a 1ª nota: '))
nota2 = int(input('Informe a 2ª nota: '))
nota3 = int(input('Informe a 3ª nota: '))

print(media(nota1, nota2, nota3))

def calcule_horas_extras(quantidade_horas, valor_hora):
    horas = float(quantidade_horas)
    taxa = float(valor_hora)

    if horas >= 40:
        valor_receber = (horas - 40) * taxa

    return valor_hora

quantidade_horas = float(input('Informe o total de horas trabalhadas: '))
valor_da_hora = float(input('Informe o valor da taxa do colaborador: '))

salario = 1500.00
print(salario + calcule_horas_extras(quantidade_horas, valor_da_hora))

def argumento(argumento_positivo, argumento_negativo):
    positivo = float(argumento_positivo)
    negativo = float(argumento_negativo)

    if positivo > 1:
        print('p')
    if negativo <= 0 or -0:
        print('n')