import json
biblioeteca = {}
cadastro= []
class Biblioeteca:
    def __init__(self, nome, autor, genero):
        self.__nome = nome
        self.__autor = autor
        self.__genero = genero
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    
    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero):
        self.__genero = genero
    
    def salvar(self):
        
        with open("C:/Users/ead/Desktop\logicaprogramacaoaula/logicaprogramacaoaulas/aula11/bib.json", "r", encoding="utf-8") as f:
                biblioteca = dict(json.load(f))
                biblioteca["livros"].append({
            "nome": self.nome,
            "autor": self.autor,
            "genero": self.genero
        })
                
        with open("C:/Users/ead/Desktop\logicaprogramacaoaula/logicaprogramacaoaulas/aula11/bib.json", "w", encoding="utf-8") as f:
            json.dump(biblioteca, f, ensure_ascii=False, indent=4)
        
        print(f"O nome do livro é : {self.nome}")
        print(f"O autor do livro é : {self.autor}")
        print(f"O gênero do livro é : {self.genero}")


  
def deletar(livro):
    global biblioeteca  
    nome = input("Digite o livro que deseja remover: ")
    encotrado = False
    for  chave,livro in list(biblioteca.items()):
        for livro in biblioeteca:
            if livro["nome"].lower() == nome in biblioeteca:
                del biblioeteca[livro]
                with open("C:/Users/ead/Desktop\logicaprogramacaoaula/logicaprogramacaoaulas/aula11/bib.json", "r", encoding="utf-8") as f:
                    json.load(biblioteca, f, ensure_ascii=False, indent=4)
                    print('Livro deletado com sucesso!')
                    encotrado = True
            else:
                print("Esse livro não esta na biblioteca!")

    if encotrado:
        exit

with open('C:/Users/ead/Desktop/logicaprogramacaoaula/logicaprogramacaoaulas/aula11/bib.json','r', encoding="utf-8") as f:
    #Abre o caminho e vai para o arquivo
    biblioteca = json.load(f)
print(30*'-', "Biblioteca", 30*'-')
def cadastrar():
    global biblioteca
    
    # Pede os dados do livro
    nome = input("Digite o título do livro: ").lower()
    autor = input("Digite o nome do autor: ").lower()
    genero= input("Digite o gênero : ").lower()

    # Descobre qual será o próximo "TituloN"
    proximo_indice = len(biblioteca) + 1
    chave = (f'{proximo_indice}')

    # Monta o livro como dicionário
    livro= {
        "nome": nome,
        "Autor": autor,
        "genero": genero
    }
    livro = Biblioeteca(nome, autor, genero)
    livro.salvar()

    # Adiciona ao dicionário principal dentro de uma lista
    biblioteca[livro] = [chave]

def menu():
    print()
    print(30*'-', "MENU", 30*"-")
    print("OPÇÃO 1 --  CADASTRAR")
    print("OPÇÃO 3 --  DELETAR")
    print("OPÇÃO 4 --  SAIR")
    print()



def sair():
    exit()
while True:
    menu()
    opcao = input("Digite uma opção: ")
    match opcao:
        case '1' :
            cadastrar()
            # Cria o objeto e cadastro
        case '3':
            deletar()

        case '4' :
            sair()
