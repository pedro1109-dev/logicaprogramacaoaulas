#lista
'''
nome_lista = ["Fulano","Ciclano", "Beltrano", "Joana", "Mariana", "Maria"]

#percorrendo
for nome in nome_lista:
    print(nome)

# percorrendo a lista com um contador 
for i in range(len(nome_lista)):
    print(f'{i+1}º nome da lista:{nome_lista[i]}')

#busca o noe desejado
nome_lista = ["Fulano","Ciclano", "Beltrano", "Joana", "Mariana", "Maria"]
nome = input("Informe o nome que deseja encontrar :")
if nome in nome_lista:
    print(nome)
else:
    print(f'{nome} não encontrado.') 

#index
nome_lista = ["Fulano","Ciclano", "Beltrano", "Joana", "Mariana", "Maria"]
nome = input("Informe o nome que deseja encontrar :")
indice = nome_lista.index(nome)
# retorna resultado
try:
    print(f'{nome} encontrado no índice : {indice}º.')
except:
    print(f'{nome} não encontrado')

#count
nome_lista = ["Fulano","Ciclano", "Beltrano", "Joana", "Mariana", "Maria","Ciclano","Ciclano","Ciclano","Ciclano","Ciclano","Ciclano"]
nome = input("Informe o nome que deseja encontrar :")
quantidade = nome_lista.count(nome)
try:
    print(f'{nome} foi encontrado na lista {quantidade} vezes.')
except :
    print(f'{nome} não foi encontrado')
#alterar
nome_lista = ["Fulano","Ciclano", "Beltrano", "Joana", "Mariana", "Maria"]
nome_a_alterar = input('Informe o nome que deseja alterar: ')
nome_lista[nome_lista.index(nome_a_alterar)] = input('Informe o novo nome: ')

for nome in nome_lista:
    print(nome
'''

#Bibliotecas
'''
    Programa : Contagem Regressva 
    importando bibliotecas
    aula04: 19/08/25
'''
# importando bibliotecas (lib)
import os
from time import sleep 

cont = input("Digite um número inteiro: ")

try:
    cont_int = int(cont)
    while cont_int >= 0: 
        os.system("cls")
        print(f"Contagem regressiva : {cont_int}")
        sleep(0.5)
        cont_int -= 1 
except:
    print("Digite um número valido!")
print("fim da contagem")

