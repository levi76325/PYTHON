# voce tem que ser privado '__'
class Automovel:
    def __init__ (self, placa, cor):
        self.placa = placa
        self.cor = cor  

    def get_placa(self):
        return self.placa
    
    def dirigir(self, velocidade):
        print(f'Estou dirigindo a { velocidade } Km/h')

    def get_cor(self):
        return self.cor
    
    def set_cor(self, nova_cor):
        self.cor = nova_cor


carro = Automovel('FDS-2211', 'vermelho')
print(carro.get_cor())
carro.set_cor('dourado')
print(carro.get_cor())


#OBS-voce deve fazer por categorias

class Automovel:
    def __init__ (self, placa='123-lev'):
        self.placa = placa

    def get_placa(self):
        return self.placa
    
    def dirigir(self, velocidade):
        print(f'Estou dirigindo a { velocidade } Km/h')

carro = Automovel()
print(carro.get_placa())
carro.dirigir(412)
# get, self e comuns
# Chamadas SET
carro.set_placa('154-VEL')