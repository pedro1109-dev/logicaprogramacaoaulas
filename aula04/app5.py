'''
    Programa : Sorteio V.5.0
    importando bibliotecas
    aula04: 19/08/25
    Random: escolha aleatoria
    Descrição:Sistema recebe o nome dos candidatos e realiza o sorteio 
'''
# importando bibliotecas (lib)
import random
import os 
import time
numero_secreto = random.randint(1,100)

tentativas = 0 
max_tentativas = 10
acertou = False 
print(30*"-", "Bem vindo ao AdvinhaLogo", 30*"-")
print(f'Você tem {max_tentativas} tentativas para advinhar o número secreto entre 1 e 100')
print("Vamos começar?")

while tentativas < max_tentativas:
    try:
        palpite = int(input("Digite seu palpite: "))
    except ValueError:
        print("Por favor digite um número válido")
        continue
    tentativas += 1 
# verificar 
    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite < numero_secreto:
        print("Tente um nùmero maior")
        print(f"Você já usou {tentativas} tentativas.")
        time.sleep(3)
        os.system("cls")
    else:
        print("Tente um número menor")
        print(f"Você já usou {tentativas} tentativas.")
        time.sleep(3)
        os.system("cls")
if acertou:
    print(f"Parabéns você é muito bomo número secreto era: {numero_secreto} ")
else:
    print(f"Você é muito burro o número secreto era: {numero_secreto} ")
