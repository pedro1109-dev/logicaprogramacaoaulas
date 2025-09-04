import random
import os
import json
#abrir pasta json
with open(fr'C:\Users\ead\Desktop\logicaprogramacaoaula\logicaprogramacaoaulas\aula08\py.json', 'r', encoding='utf-8') as f:
    temas = json.load(f)
def sair():
    exit()

def menu():
    while True:
        p= [['Tema 1 - Palvras aleatorias.'],
            ['Tema 2 - comida.'],
            ['Tema 3 - animais.'],
            ['4- Sair do sistema.']]
        for i in p :
            print(i)
        #recebe a escolha do usuario
        opcao = input('Escolha uma opção: ')
        #verifica a escolha
        match opcao:
            case '1':
                return random.choice(temas["tema1"])
            case '2':
                return random.choice(temas["tema2"])
            case '3':
                return random.choice(temas["tema3"])
            case '4':
                return sair()
            case _:
                continue

def jogar_forca():
    palavra = menu()
    letras_corretas = []
    letras_erradas = []
    tentativas= 6
    #Após receber o tema, verifica erro e acerto
    while True:
        palavra_escondida= ''
        for letra in palavra:
            if letra in letras_corretas:
                palavra_escondida += letra
            else:
                palavra_escondida +='_'
        print('Palavra: ', palavra_escondida)
        print('Letras erradas:', letras_erradas)
        print('Tentativas restantes:', tentativas)
        #Tela de vitória se o usuário acertar tudo
        if palavra_escondida == palavra:
            print('Parabens!Você ganhou!!!!')
            break
        elif tentativas == 0 :
            print('Você perdeu! A palavra era:',palavra)
            break
        #Recebe a letra do usuário
        letra_usuario = input('Digite uma letra: ').lower()
        #diminui tentativas se a letra for errada
        if letra_usuario in palavra:
            print('Letra correta')
            letras_corretas.append(letra_usuario)
        else:
            print('Você errou a letra')
            letras_erradas.append(letra_usuario)
            tentativas -= 1

#Execução do sistema
if __name__=='__main__':
    os.system('cls')
    print('Bem vindo ao jogo da forca!!')
    jogar_forca()
    
