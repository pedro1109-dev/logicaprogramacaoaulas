contas = {}
proximo_numero = 1
def menu(): 
    print()
    print('1-Criar conta')
    print('2-Exibir dados')
    print('3-Sacar')
    print('4-Depositar')
    print('5-Excluir conta')
    print('6- Sair do sistema!')
    print()


def exibir_dados():
    if not contas :
        print('Nenhuma conta encotrada!')
        return
    for numero, dados in contas.items():
        print()
        print(f'Conta : {numero}')
        print(f'Saldo : {dados['saldo']}')
        print(f'Cliente : {dados['nome']} | CPF: {dados['cpf']}')
        print()

def criar_conta():
    global proximo_numero
    nome = input('Digite seu nome: ').strip()
    cpf = input('Digite seu cpf: ')
    contas[proximo_numero] = {'nome':nome, 'saldo':0.0, 'cpf':cpf}
    print(f'Conta criadad com sucesso!Número da conta: {proximo_numero}')
    proximo_numero += 1

def depositar():
    numero = int(input('Digite o número da conta: '))
    if numero in contas: 
        valor = float(input('Digite o quanto quer depositar: '))
        contas[numero]['saldo'] += valor
        print(f"Deposito de {valor} realizado com sucesso!")

def sacar():
    numero = int(input('Digite o número da sua conta: '))  
    if numero in contas:
        valor = float(input('Digite o valor que quer sacar: ')) 
        contas[numero]['saldo'] -= valor
        print(f'Saque de {valor} realixados com sucesso!')
def excluir_conta():
    numero = int(input('Digite o número da sua conta: '))
    if numero in contas:
        del contas[numero]
        print('Conta excluída com sucesso')

def sair():
    exit()


while True:
    menu()
    opcao = input("Digite a opção desejada: ")
    if opcao == '1':
        criar_conta()
    elif opcao == '2':
        exibir_dados()
    elif opcao == '3':
        sacar()
    elif opcao == '4':
        depositar()
    elif opcao == '5':
        excluir_conta()
    elif opcao == '6':
        sair()
        break
    else:
        print('Opção inválida')


