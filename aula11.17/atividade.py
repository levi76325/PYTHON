''
contador = 0
while contador < 20:
    idade_aluno = int(input('informe sua idade: '))
    if idade_aluno > 13:
        print(f'o Aluno {contador} tem mais de 13 anos')
    contador =+ 1 


 
while True:
    nota = int(input('informe a nota: '))
    if nota < 0 or nota > 10:
        break