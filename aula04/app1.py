'''
    Programa : Sorteio V.1.0
    importando bibliotecas
    aula04: 19/08/25
    Random: escolha aleatoria
    Descrição:Sistema recebe o nome dos candidatos e realiza o sorteio 
'''
# importando bibliotecas (lib)
import random 
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")
nome4 = input("Digite o quarto  nome: ")
nome5 = input("Digite o quinto nome: ")
lista_nomes = [nome1, nome2, nome3, nome4, nome5 ]

escolhido = random.choice(lista_nomes)
print(f"Nome escolhido: {escolhido}")