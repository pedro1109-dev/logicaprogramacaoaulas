'''
    Programa : Sorteio V.3.0
    importando bibliotecas
    aula04: 19/08/25
    Random: escolha aleatoria
    Descrição:Sistema recebe o nome dos candidatos e realiza o sorteio 
'''
# importando bibliotecas (lib)
import random
import os
import time

lista_nomes = []
lista_sorteados = []

while True:
    nome = input("Digite o nome para o sorteio: ")
    if nome:
        lista_nomes.append(nome)
    else:
        break

while True:
    if lista_nomes: 
        os.system("cls")
        escolhido = random.choice(lista_nomes)
        lista_sorteados.append(escolhido)

        print(f'O escolhido foi :{escolhido}')

        lista_sorteados.remove(escolhido)

        opcao = input("Deseja sortear outro nome ? S - Sim \n| N - Não\n: ").lower()
        os.system("cls")

        if opcao != "s":
            break
    else:
        print("Não há nomes para ser sorteados")
        break
    print("Programa finalizado")
    print(f"Os nomes sorteados foram {lista_sorteados}")