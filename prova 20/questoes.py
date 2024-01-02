
class Viagem:
    def __init__(self):
        self.viajante = input("Digite o nome do viajante: ")
        self.destinos = ["Praia", "Montanha", "Cidade"]

    def escolher_destino(self):
        print("Opções de destinos:")
        for i, destino in enumerate(self.destinos, start=1):
            print(f"{i}. {destino}")

        escolha = int(input("Digite o número do destino desejado: "))
        if 1 <= escolha <= len(self.destinos):
            destino_escolhido = self.destinos[escolha - 1]
            print(f"{self.viajante}, você escolheu o destino: {destino_escolhido}")
        else:
            print("Opção inválida. Escolha um número válido.")

# Criando uma instância da classe Viagem
minha_viagem = Viagem()
minha_viagem.escolher_destino()





class FeiraLivre:
    def __init__(self):
        self.frutas = ["Maçã", "Banana", "Laranja", "Uva", "Pera"]

    def exibir_frutas(self):
        print("Bem-vindo à feira livre! Aqui estão as opções de frutas:")
        for i, fruta in enumerate(self.frutas, start=1):
            print(f"{i}. {fruta}")

    def escolher_fruta(self):
        nome_solicitante = input("Digite seu nome: ")
        self.exibir_frutas()
        escolha = int(input("Digite o número da fruta desejada: "))

        if 1 <= escolha <= len(self.frutas):
            fruta_escolhida = self.frutas[escolha - 1]
            print(f"{nome_solicitante}, você escolheu a fruta: {fruta_escolhida}")
        else:
            print("Opção inválida. Escolha um número válido.")

# Criando uma instância da classe FeiraLivre
minha_feira = FeiraLivre()
minha_feira.escolher_fruta()




class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        novo_contato = Contato(nome, telefone)
        self.contatos.append(novo_contato)
        print(f"Contato {nome} adicionado com sucesso!")

    def editar_contato(self, nome, novo_telefone):
        for contato in self.contatos:
            if contato.nome == nome:
                contato.telefone = novo_telefone
                print(f"Contato {nome} atualizado com o novo telefone: {novo_telefone}")
                return
        print(f"Contato {nome} não encontrado.")

    def excluir_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print(f"Contato {nome} excluído com sucesso!")
                return
        print(f"Contato {nome} não encontrado.")

    def listar_contatos(self):
        print("Lista de contatos:")
        for contato in self.contatos:
            print(f"{contato.nome}: {contato.telefone}")

# Criando uma instância da classe Agenda
minha_agenda = Agenda()

# Exemplo de uso
minha_agenda.adicionar_contato("Maria", "123456789")
minha_agenda.adicionar_contato("João", "987654321")
minha_agenda.listar_contatos()

minha_agenda.editar_contato("Maria", "999999999")
minha_agenda.listar_contatos()

minha_agenda.excluir_contato("João")
minha_agenda.listar_contatos()


class BombaCombustivel:
    def __init__(self, tipo_combustivel="G"):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = 0

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel

    @tipo_combustivel.setter
    def tipo_combustivel(self, tipo):
        tipo = tipo[0].upper()

        if tipo == "G":
            print("Tipo GASOLINA selecionado")
            self.__tipo_combustivel = "GASOLINA"
            self.valor_litro = 3.24
        elif tipo == "A" or tipo == "Á":
            print("Tipo ÁLCOOL selecionado")
            self.__tipo_combustivel = "ÁLCOOL"
            self.valor_litro = 2.37
        else:
            print("Tipo selecionado não é válido")

    def abastecer_por_valor(self):
        if self.valor_litro == 0:
            print("Selecione um tipo de combustível válido")
        else:
            valor = float(input("\nAbastecer Valor (R$): "))
            litros = valor / self.valor_litro
            print(f"Abastecido {litros:.2f} litros de {self.tipo_combustivel}")

    def abastecer_por_litro(self):
        if self.valor_litro == 0:
            print("Selecione um tipo de combustível válido")
        else:
            litros = float(input("\nQuantidade de litros: "))
            valor_pagar = litros * self.valor_litro
            print(f"Valor a ser pago: R$ {valor_pagar:.2f}")


# Exemplo de uso
bomba = BombaCombustivel()
bomba.abastecer_por_valor()
bomba.abastecer_por_litro()



class Cafeteira:
    compartimento_filtro = False
    compartimento_agua = False
    cafe_pronto = False
    ligada = False

    def ligar(self):
        self.ligada = True
        print('Cafeteira Ligada')

    def desligar(self):
        self.ligada = False
        self.compartimento_agua = False
        self.compartimento_filtro = False
        self.cafe_pronto = False
        print('Cafeteira Desligada')

    def colocar_agua(self):
        if self.ligada == True:
            self.compartimento_agua = True

    def colocar_filtro(self):
        if self.ligada == True:
            if self.compartimento_filtro == False:
                self.compartimento_filtro = True

    def fazer_cafe(self):
        if self.ligada == True and self.compartimento_filtro == True and self.compartimento_agua == True:
            self.cafe_pronto = True
        else:
            print('Verifique os compartimentos')

    def valida_cafe(self):
        if self.cafe_pronto == True:
            return 'Pronto'
        else:
            return 'Aguarde...'

    def valida_ligada(self):
        if self.ligada == True:
            return 'Ligada'
        else:
            return 'Desligada'

    def valida_filtro(self):
        if self.compartimento_filtro == True:
            return 'com filtro'
        else:
            return 'sem filtro'
    
    def valida_agua(self):
        if self.compartimento_agua == True:
            return 'com agua'
        else:
            return 'sem agua'
          
    def __str__(self):
        return f'A cafeteira está { self.valida_ligada() }, o compartimento de agua está { self.valida_agua() }, o compartimento do filtro está { self.valida_filtro() }. E o café: { self.valida_cafe() },'
    

minha_cafeteira = Cafeteira()

print(minha_cafeteira)

minha_cafeteira.ligar()

print(minha_cafeteira)

minha_cafeteira.fazer_cafe()

minha_cafeteira.colocar_agua()

print(minha_cafeteira)

minha_cafeteira.colocar_filtro()

print(minha_cafeteira)

minha_cafeteira.fazer_cafe()

print(minha_cafeteira)


class Televisao:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.canal = 0
        self.ligada = False

    # GETs
    def get_tamanho(self):
        return self.tamanho
    
    def get_canal(self):
        return self.canal 
    
    

    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
    
    def set_canal(self, novo_canal):
        if self.ligada == True and novo_canal >= 0 and novo_canal <= 999:
             self.canal = novo_canal

  
    def ligar(self):
        self.ligada = True
        print('Sua TV está Ligada')

    def desligar(self):
        self.ligada = False
        print('Sua TV está Desligada')

    def valida_ligada(self):
        if self.ligada == True:
            return 'Ligada'
        else:
            return 'Desligada'

    def __str__(self):
        return f'Sua TV está { self.valida_ligada() } o canal está em { self.canal } e o tamanho dela é { self.tamanho } polegadas'

# Chamadas de Criação
minha_tv = Televisao(32)

minha_tv.ligar()
minha_tv.desligar()

minha_tv.ligar()
minha_tv.set_canal(10)

print(minha_tv.get_canal())

print(minha_tv)


# dunder metodo => __metodo__
class Estudante:
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula
        self.nome_classe = self.__class__.__name__
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    cpf = property(get_cpf, set_cpf)

class EstudanteGraduacao(Estudante):
    def __init__(self, curso, nome, matricula):
        self.curso = curso
        super().__init__(nome, matricula)
        
    
    def __str__(self):
        return f'A sua classe é { self.nome_classe }. Olá, { self._nome } seu CPF é: { self.get_cpf() } seu curso de Graduação é o de { self.curso } e sua matricula de acesso é { self._matricula }'

class EstudantePos(Estudante):
    nivel = 1
    orientador = 'Prof Carlos Alberto'

    def __str__(self):
        return f'A sua classe é { self.nome_classe }.Olá, { self._nome } seu nivel é { self.nivel }° e seu Tutor será o { self.orientador }. para seu acesso utilize a matricula { self._matricula }'

aluno1 = EstudanteGraduacao('ADS', 'Paulo Junior', 353637)
# aluno2 = EstudantePos('Paulo Junior', '565758')


aluno1.set_cpf(123456789)
print(aluno1.get_cpf())
print(aluno1)
# print(aluno2)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__cpf = None
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, meu_cpf):
        self.__cpf = meu_cpf

class Professor(Pessoa):
    def __init__(self, nome, idade, salario, disciplina, cpf):
        super().__init__(nome, idade)
        self.salario = salario
        self.disciplina = disciplina
        self.cpf = super().set_cpf(cpf)
    
    def __str__(self):
        return f'Nome: { self.nome }, Idade: { self.idade } e CPF: { self.get_cpf() } Salario: { self.salario }, Disciplina: { self.disciplina }.'
    
class Aluno(Pessoa):
    pass

paulo = Professor('Paulo Junior', 29, 1400.00, 'Backend', 1234567890)

print(paulo)


# crie abstração para uma super classe funcionario com duas subclasses. Imprima todos do dados.

class Funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def get_nome(self):
        return self.nome 
    
    def get_salario(self):
        return self.salario
    
    
class Gerente(Funcionarios):
    pass

class Desenvolvedor(Funcionarios):
    pass



class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} está ligado.")
        else:
            print(f"O {self.modelo} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O {self.modelo} está desligado.")
        else:
            print(f"O {self.modelo} já está desligado.")

# Exemplo de uso
meu_carro = Carro(cor="Azul", modelo="Sedan")
meu_carro.ligar()
meu_carro.desligar()
