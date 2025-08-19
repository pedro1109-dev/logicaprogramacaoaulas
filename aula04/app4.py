'''
    Programa : Sorteio V.4.0
    importando bibliotecas
    aula04: 19/08/25
    Random: escolha aleatoria
    Descrição:Sistema recebe o nome dos candidatos e realiza o sorteio 
'''
# importando bibliotecas (lib)
from random import randint

print("Tente advinhar o número!")
num1 = int(input("Digite um número: "))

num_secret = randint(1,1000)
if num1 == num_secret:
    print("Parabéns,você ganhou")
else:
    print("Voicê perdeu")
    print(f"O número correto é {num_secret}")