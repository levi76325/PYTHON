class Televisao:
    def __init__(self, tamanho):
        self.tamanho = 0 
        self.canal = 0 
        self.ligada = False

    def get_tamanho(self):
        return self.tamanho
    
    def get_canal(self):
        return self.get_canal
    
    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

    def set_canal(self, novo_canal):
        if self.ligada == True and novo_canal >= 0 or novo_canal <= 100:
                self.canal = novo_canal

    def ligar(self):
        self.ligar = True
        return self.ligar #ou print('sua tv esta ligada')

    def desligar(self):
        self.desligar = False
        return self.desligar


def __str__(self):
    return f'Sua Tv esta { self.ligada} o canal esta no { self.canal} e o tamanho dela ela de { self.tamanho}'

# chamadas de criação
minha_tv = Televisao(32)

minha_tv.ligar()
minha_tv.desligar()

minha_tv.set_canal()

minha_tv.get_canal()