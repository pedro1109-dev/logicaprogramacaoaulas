#revisao
'''
problema:crie um sistema que calcule o indice de massa corporal(IMC)
do usuario, mostre o valor do imc na tela, retorne se o usuario esta
no peso ideal ou se precisa emagrecer ou engordar mais. Utilize a tabela
'''
'''
print(40*'-','CALCURADORA DE IMC',40*'-')
while True :
    nome_usuario = input('Digite seu nome:')
    peso = float(input('Digite seu peso :').replace(',','.'))
    altura = float(input('Digite sua altura:').replace(',','.'))

    imc = peso / (altura*altura)
    print()
    print(f'Seu IMC é:{imc:.2f}')
    if imc <= 18.5:
        print(f'{nome_usuario} seu IMC está abaixo do normal.')
    elif imc <= 24.9:
        print('Seu IMC está normal.')
    elif imc <= 29.9:
        print('Você stá com sobrepeso.')
    elif imc <= 34.9:
         print('Obesidade grau I')
    elif imc <= 39.9:
        print('Obesidade grau I')
    else :
        print('Obesidade grau III')

    opcao = input('Deseja calcular novamente? S - Sim | N-Não)').lower()

    if opcao == 's':
        continue
    elif opcao == 'n':
        print('Saindo do sistema!')
        break
    else:
        print('Opção inválida')
'''


'''
Problema 2 : Um elevador de carga possui capacidade para 200kg. Crie 
um programa que rceba do usuario seu peso e o peso da carga e verificar se a carga está autorizada 
a usar o elevador ou não
'''
'''
print(40*'-', ' Aviso do limite de peso do elevador', 40*'-')
limite_carga = 200 
carga_usuario = float(input('Digite o peso da sua carga aqui: '))
peso_usuario = float(input('Digite seu peso aquo:'))
carga_total = carga_usuario + peso_usuario
if carga_total <= limite_carga :
    print(f'A carga total está dentro do limite de 200kg. sua carga é: {carga_total}'.replace(',','.'))
else:
    print(f'A carga total excede o limite de 200kg, sua carga é: {carga_total}'.replace(',','.'))
'''
'''
numero = int(input('Digite um numero:'))
while numero >= 0:
    print(numero)
    numero -= 1 
'''

print(40*'-','CADASTRO DE USUARIO',40*'-')
nome = input("Digite seu nome: ")
CPF = input('Digite sey CPF: ')
num = input('Digite seu numero: ')
data_nasc = float(input('Digite sua data de nascimento: '))

while True:
    print(40*'-','Sistema Console 2º DS',40*'-')
    print()
    print('1 - Calculadora IMC')
    print('2- Maioridade')
    print('3- Calculadora')
    print('4- Dados Pessoais')
    print('5- feliz Natal')
    print('6-Sair')

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        nome_usuario = input('Digite seu nome:')
        peso = float(input('Digite seu peso :').replace(',','.'))
        altura = float(input('Digite sua altura:').replace(',','.'))

        imc = peso / (altura*altura)
        print()
        print(f'Seu IMC é:{imc:.2f}')
        if imc <= 18.5:
            print(f'{nome_usuario} seu IMC está abaixo do normal.')
        elif imc <= 24.9:
            print('Seu IMC está normal.')
        elif imc <= 29.9:
            print('Você stá com sobrepeso.')
        elif imc <= 34.9:
            print('Obesidade grau I')
        elif imc <= 39.9:
            print('Obesidade grau I')
        else :
            print('Obesidade grau III')
        

    elif opcao == '2' :
        ano_atual = '2' 
        idade = ano_atual - data_nasc
        print(nome , 'é maior de idade.' if idade >= 18 else 'é mneor de idade' )
    elif opcao == '3' :
        print(50*"-")
        while True:
            numero1 = int(input("Digite o primeiro numero:"))
            numero2 = int(input("Digiteo segundo numero:"))
            print('1- Soma')
            print('2- Divisão')
            print('3- Subtração')
            print('4- Multiplicação')
            print('5- Sair')
            opcao_calculo = input("Escolha uma opção matemática")

            if opcao_calculo == "1" :
                print(f'Resultado da soma é: {numero1 + numero2}')
            elif opcao_calculo == "2" :
                print(f"Resultado da divisao é: {numero1 +numero2}")
            elif opcao_calculo == "3" :
                print(f"Resultado da subtraçao é: {numero1 +numero2}")
            elif opcao_calculo == "4" :
                print(f"Resultado da multiplicaçao é: {numero1 +numero2}")
            elif opcao_calculo == "5" :
                break

    elif opcao == '4' :
        print(50*'-')
        print(f'Nome: {nome} |CPF:{CPF}')
        print(f'numero: {num} |data de nascimento:{data_nasc}')
        print(20*'-')
    elif opcao == '5' :
        linhas = 20
        j = 1 

        while j <= linhas:
            espacos = linhas - j
            estrelas = 2 * j - 1 
            print(' ' * espacos + '⁊' * estrelas)
            j +=1
    elif opcao == '6' :
        print('Saindo do sistema')
        break
    else:
        print('Opção invalida!')
        

