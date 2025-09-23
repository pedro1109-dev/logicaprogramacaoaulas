class Corredor:
    def __init__(self, corredor, vida):
        self.__nome = corredor
        self.__vida = vida
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    def atacar(self, personagem):
        personagem.vida -= 50
        print(f'{self.nome} atacou {personagem.nome} e tirou 50 pontos de vida.')
        print(f'Agora esta com {personagem.vida}')
        if personagem.vida == 0 :
            print("Sua torre caiu!")
        else:
            print("Sua torre ainda está de pé!")


    def torre(self, personagem):
        personagem.vida -= 40
        print(f'{self.nome} atacou {personagem.nome} e tirou 40 pontos de vida.')
        print(f'Agora o corredor está com {personagem.vida}')

personagem1 = Corredor('Corredor', 100)
personagem2 = Corredor('Torre', 100)

personagem1.atacar(personagem2)
personagem2.torre(personagem1)