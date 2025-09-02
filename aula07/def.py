#Funcoes
cadastro = []

import os
limpar = lambda: os.system('cls' if os.name == 'nt'else 'clear')
def menu(): 
    print()
    print('1-Criar conta')
    print('2-Exibir dados')
    print('3-Sacar')
    print('4-Depositar')
    print('5-Excluir conta')
    print()

def exibir_dados():
    print()
    print('Conta:')
    print('Banco:')
    print('Saldo:')
    print('Cliente:')
    print()

def sacar():
    ...
def deposito(deposito, saldo):
    return deposito + saldo
def cadastrar():
    cadastro
def excluir_conta():
    ...
usuario = {}
numero = {}
usuario['nome'] = input('Informe o nome: ').strip().title()
numero['número'] = input('Informe seu número: ')
while True :
    print('1-Menu.')
    print('2-Exibir Dados.')
    print('3-Saque')
    print('4-Deposito.')
    print('5-Excluir.')
    opcao = input('Digite uma das opções:')
    match opcao :
        case '1':
            menu()
        case '2':
            exibir_dados()
        case '3':
            ...
        case '4' :
            ...
        case '5':
            break
