# a condição ternaria acontece em formato de linha.

salario = float(input('Informe o valor do seu salario: '))
if salario >= 2500.00:
    print("IR sera cobrado")

else:
    print("IR não sera cobrado!")


variavel_controle = 'IR sera cobrado' if salario >= 2500.00 else 'IR nao sera cobrado'

print(variavel_controle)

vr_contrale = 'OK 1' if True else 'OK 2' if False else 'Fim'

print(vr_contrale)

if True:
    print('OK 1')

elif True:
    print('OK 2')
else:
    print('Fim')