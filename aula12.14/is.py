#
'''
numero = input("Digite um numero: ")
if numero.isdigit() == True:
    print('E um numero.....')

'''

class Pet:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.fome = 0
        self.sede = 0 
        self.comida = 100
        
    def get_nome(self):
        return self.nome
    def get_peso(self):
        return self.peso
    def get_fome(self):
        return self.fome
    def get_sede(self):
        return self.sede
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def set_peso(self, novo_peso):
        self.peso = novo_peso
        
    def set_fome(self, novo_fome):
        if self.fome >= 99:
            print(f'Alimente o { self.nome} pois a fome dele esta em {self.fome}')
            nova_comida = int(input('Quanto de comida vc quer dar ao cao: '))
            self.comida -= nova_comida
            self.fome = novo_fome
        else:
            self.fome += novo_fome
        
    def set_sede(self, novo_sede):
        self.sede= novo_sede

    def imprimir(self):
        print(f'Ola, me chamo {self.nome}')
        print(f'Estou pesando { self.peso} Kg')
        print(f'minha fome esta em { self.fome}')
        print(f'minha sede esta em { self.sede}')
cao = Pet('jahlán bihpal',24)

cao.imprimir()
cao.set_fome(2)
cao.set_sede(0)

cao.imprimir()
cao.set_fome(30)
cao.set_sede(35)

cao.imprimir()
cao.set_fome(70)
cao.set_sede(35)

cao.imprimir()
cao.set_fome(10)
cao.set_sede(35)
