class Personagem:
    # construtor
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida
    #definindo GET e SET
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
        personagem.vida -= 20
        print(f'{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida.')
        print(f' Agora {personagem.nome} está com {personagem.vida}')

class Pekka(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self, personagem):
        personagem.vida -= 950
        print(f'{self.nome} atacou {personagem.nome} e causou 950 de dano')
        if personagem.vida <= 1:
            print('Personagem morto')
        else:
            print(f'A vida do {personagem.nome} é : {personagem.vida}')
            
class Princesa(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self, personagem):
        personagem.vida -= 144
        print(f'{self.nome} atacou {personagem.nome} e causou 144 de dano')
        if personagem.vida <= 1:
            print('Personagem morto')
        else:
            print(f'A vida do {personagem.nome} é : {personagem.vida}')
            
class MegaCavaleiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
    
    #definindo GET e SET
    def pouso(self, Personagem):
        Personagem.vida -= 500
        print(f'{self.nome} pousou na arena e deu 500 de dano inicial em {Personagem.nome}!')
        print(f' Agora {Personagem.nome}está com {Personagem.vida}')

        
 
    # sobrescrevendo o metodo da classe Pai
    def atacar(self, personagem):
        personagem.vida -= 350
        print(f'{self.nome} atacou {personagem.nome} e causou 350 de dano')
        if personagem.vida <= 1:
            print('Personagem morto')
        else:
            print(f'A vida do {personagem.nome} é : {personagem.vida}')
            

class Canhoneiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        
        
 
    # sobrescrevendo o metodo da classe Pai
    def atacar(self, personagem):
        personagem.vida -= 350
        print(f'{self.nome} atacou {personagem.nome} e causou 350 de dano')
        if personagem.vida <= 1:
            print('Personagem morto')
        else:
            print(f'A vida do {personagem.nome} é : {personagem.vida}')
    

canhao = Canhoneiro('canhoneiro' , 3456)
print(30*'-', 'Lado Vermelho',30*'-')
print(f'Torre: {canhao.nome}')
print(f'Vida: {canhao.vida}')
personagemfav = MegaCavaleiro('MegaCavaleiro' , 2300)
print(f'Personagem: {personagemfav.nome}')
print(f'Vida: {personagemfav.vida}')

print(30*'-', 'Lado Azul',30*'-')
pekka = Pekka('Pekka', 4900)
print(f'Personagem: {pekka.nome}\n Vida: {pekka.vida}')
princesa = Princesa('Princesa', 4032)
print(f'Torre: {princesa.nome}\n Vida: {princesa.vida}')
print(30*'-', 'Batalha',30*'-')

personagemfav.pouso(pekka)
pekka.atacar(personagemfav)
personagemfav.atacar(pekka)
princesa.atacar(personagemfav)
canhao.atacar(pekka)
pekka.atacar(personagemfav)
personagemfav.atacar(pekka)
princesa.atacar(personagemfav)
canhao.atacar(pekka)
pekka.atacar(personagemfav)


if personagemfav.vida <= 1 :
    print(f'temos um vencedor!: {pekka.nome}')

elif pekka.vida <= 1:
    print(f'temos um vencedor!: {personagemfav.nome}')

else:
    pass
