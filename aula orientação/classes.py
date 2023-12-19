'''
class FoneDeOuvido:
    def get_volume(self):
        return self.volume
    def set_volume(self, novo_volume):
        self.volume = novo_volume

    volume = property(get_volume, set_volume)


fone = FoneDeOuvido(25)

fone.set_volume(20)

print(fone.get_volume())
'''




# na prova tem q ligar e desligar 


'''
class ControleRemoto:
    def __init__(self, cor, marca, qtd_pilhas):
        self.botao = None
        self.cor = cor
        self.marca = marca
        self.qtd_pilhas = qtd_pilhas
        self.painel = False
        self.temperatura = 0

    # METODOS
    def ligar(self):
        self.painel = True

    def desligar(self):
        self.painel = False 

    def set_temperatura(self, nova_temperatura):
        if self.painel == False:
            print('Temperatura não pode ser alterada, O Ar Desligado')
        else:
            self.temperatura = nova_temperatura
    
    def get_temperatura(self):
        return self.temperatura
    
    def pressionar_botao(self, tipo_de_botao):
        self.botao = tipo_de_botao
        if self.botao == 'Ligar' and self.temperatura == 0:
            print('Ar está ligado')
            self.ligar()
        elif self.botao == 'Desligar':
            print('Ar está desligado')
            self.set_temperatura(0)
            self.desligar()

controle = ControleRemoto('branca', 'elgin', 2)

controle.pressionar_botao('Ligar')

controle.set_temperatura(20)

print(controle.get_temperatura())

controle.pressionar_botao('Desligar')

controle.set_temperatura(16)

print(controle.get_temperatura())


'''

'''
class FoneDeOuvido:

    def get_volume(self):
    print('entrei no get')
        return self.__volume
    
    def set_volume(self, novo_volume):
    print('entrei no set')
        self.__volume = novo_volume

    volume = property(get_volume, set_volume)

fone = FoneDeOuvido()

fone.volume = 200 # SET

print(fone.volume) # GET
'''

'''
class Automovel:
    def __init__(self, placa, cor):
        self.__placa = placa
        self.__cor = cor

    def get_placa(self):
        return self.__placa
    
    def get_cor(self):
        return self.__cor

    def set_cor(self, nova_cor):
        self.__cor = nova_cor

    def dirigir(self, velocida):
        print(f'Estou dirigindo a { velocida }km/h.')

#Instancias
carro = Automovel('TYT-0019', 'azul')
moto = Automovel('GJG-1716', 'preta')
caminhao = Automovel('AAP-1122', 'amarelo') 

# Chamadas GET
print(f'A cor do carro é { carro.get_cor()} ')
print(f'A cor da moto é { moto.get_cor()} ')
print(f'A cor do caminhão é { caminhao.get_cor()} ')

print(f'A placa do carro é { carro.get_placa()} ')
print(f'A placa da moto é { moto.get_placa()} ')
print(f'A placa do caminhão é { caminhao.get_placa()} ')

# Chamadas SET
carro.set_cor('branco')
moto.set_cor('azul')
caminhao.set_cor('preto')

carro.__cor = 'verde'


# Novas chamadas GET
print(f'A nova cor do carro é { carro.get_cor()} ')
print(f'A nova cor da moto é { moto.get_cor()} ')
print(f'A nova cor do caminhão é { caminhao.get_cor()} ')

'''