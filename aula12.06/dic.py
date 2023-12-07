'''
# CRUD = created - readed - updated - deleted
dic = { 'nome': 'paulo'} # Created
dic2 = dict( idade=23 )

print(dic)

dic['nome'] #readed
reading = dic2.get('idade') #readed

dic.update(sobrenome='junior') #update 

dic.update({ 'idade': 23 })

tupla = ('peso', 72.12),
lista = ['data', '13/04/1996'],['numeros',[1, 2, 3, 4, 5, 6, 7, 8, 9]] #updated
dic.clear() # deleted
dic.update(lista)
dic.update(tupla)
print(dic)
print(dic2)
print(f'dados do dicionario: { dic }')

lista_alunos = [['joao', 5], ['maria', 7], ['pedro', 8], ['junior', 9]]
dici = {}
dici.update(lista_alunos)
print(dici)
'''
'''
marca = input("Qual a marca do carro? ")
modelo= input("Qual o modelo do carro? ")
lista_de_carros = ()
lista_de_carros.append(marca)
lista_de_carros.append(modelo)

dic_carros = {}
dic_carros(lista_de_carros)
print(lista_de_carros)
print(dic_carros)


'''

'''
nome = input("Qual seu nome?: ")
idade = input("Qual sua idade?: ")
data_aniversario  = input("Qual a data do seu aniversario?: ")
endereco = input("Qual seu indereço completo(Rua, numero e bairro)?: ")
dicio = {}
dicio.update(nome)
dicio.update(idade)
print(dicio)

'''

'''
dic_acesso = { 'paulo': '123456', 
              'joao': '1234567'}

usuario_senha = {}

usuario = input("INforme seu usuario: ")
senha = input("Informe sua senha: ")

usuario_senha = {usuario: senha}

for chave in dic_acesso.keys():
    print(chave)
    if chave == usuario:
        print('Usuario OK!!')
        if dic_acesso[chave] == usuario_senha[usuario]:
            print("Acesso liberado!")
            break
        else:
            print(f'senha incorreta para o usuario { usuario }!')
            break
else:
    print('Usuario incorreto!')
    
'''


dic_perguntas = { 'pergunta': 'alguma coisa aqui',
                  'Opções': '[1, 2, 3, 4]',
                  'respostas': 4,
                 }



# MATRIZES EM PYTHON
'''
matriz = [[1],[2],[3],
          [4],[5],[6],
          [7],[8],[9],]

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],]

matriz = {[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],}
'''