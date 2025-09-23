# classe - Espaço onde vou descrever um objeto
# atributos - Caracteristicas do objeto
# metodos  - que sao as ações desse objeto

#nome e vida - atacar
#self - quando quero me referir a algum atributo da classe 
#contrutor - quando quero criar um novo objeto, champ o construtor
class Personagem:
    #construtor
    def __init__(self, nome, vida):
        #encapsulamento
        self.__nome = nome
        self.__vida = vida

    #definindo GET e SET
    @property
    def nome(self):
        return self.__nome
    
    #definindo SET
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida
    #metodos
    def atacar(self, personagem):
        personagem.vida -= 20
        print(f'{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida.')
        print(f'Agora esta com {personagem.vida}')

class Guerreiro(Personagem):
    def __init__(self, nome, vida, escudo=True):
        super().__init__(nome, vida)
        self.__escudo = escudo

    @property
    def escudo(self):
        return self.__escudo
    
    @escudo.setter
    def escudo(self, escudo):
        self.__escudo = escudo

#sobreescrevendo um metodo da class python
    def atacar(self, personagem):
        personagem.vida -= 40
        print(f'{self.nome} atacou {personagem.nome} e tirou 40 pontos de vida.')
        print(f'Agora esta com {personagem.vida}')

    def protecao(self):
        self.__vida += 10



class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
    
    def atacar(self, personagem):
        personagem.vida -= 30
        print(f'{self.nome} atacou {personagem.nome} e tirou 40 pontos de vida.')
        print(f'Agora esta com {personagem.vida}')

    def curar(self, personagem):
        personagem.vida += 15
        print(f'{self.nome} usou poder de cura em {personagem.nome}')
        print(f'A vida de {personagem.nome} agora é de {personagem.vida}')

frodo = Personagem('Frodo',100)
gandof = Mago('Gandof',100)
aragorn = Guerreiro('Aragorn', 100)

aragorn.atacar(frodo)
gandof.curar(frodo)
gandof.atacar(aragorn)
aragorn.atacar(gandof)
gandof.curar(gandof)
frodo.atacar(aragorn)