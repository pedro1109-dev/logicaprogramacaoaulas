nome = "Pedro"
idade = "16"
numero = "11/09/2008"
print("Ola eu me chamo:",nome , "tenho", idade, "anos de idade, e nasci no dia:", numero)

# tipos de variaveis 

nome = "pedro"
idade = 16
altura = 1.80
ativo = True 

print("o tipo de variavel nome é:", type(nome))
print("o tipo de variavel idade é:", type (idade))
print("o tipo de variavel altura é:", type(altura))
print("o tipo de variavel ativo é:", type(ativo))

print()
print(30*"-", "operadores aritmericas", 30*"-")
'''
#Operadores
num1= 5
num2 =5

soma =num1+num2
divi = num1/num2 #divisao comum
divisao_inteira = num1 // num2 #divisao interira
mult = num1*num2
expo = num1 ** num2 
sub  = num1-num2 

resto = num1 %2

print("Resultado da soma", num1, "+", num2,"é:", soma)
print("Resultado da divisao", num1, "/", num2,"é:", divi)
print("Resultado da subtraçao", num1, "-", num2,"é:", sub)
print("Resultado da multiplicaçao", num1, "X", num2,"é:", mult)
print("Resultado da divisao interia", num1, "/", num2,"é:", divisao_inteira)
print("Resultado do resto de", num1, "/", num2,"é:", resto)
print("O resultado exponencial", num1, "**", num2,"é:", expo)
 
print()
print(30*"-", "operadores de comparação", 30*"-")
# operadores de comparação

num1 > num2
num1 < num2
num1 == num2
num1 >= num2
num1 <= num2
num1 != num2

ano = 2025
print("ano atual:", ano)
ano += 1
print("Ano decrescido de +1:", ano)
ano -=1
print("Ano drececido de -1:", ano)

#operadores logicos 
# AND, OR,NOT 
#Entradas de dados

print()
print(30*"-", "Entradas de dados", 30*"-")

nome_usuario = input("Digite o seu nome: ")
print("Seja bem-vindo ao sistema python", nome_usuario, ".", "Parabens!")

print()
print(30*"-", "Digite o primeiro número", 30*"-")
 
num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digiteo segundo numero:"))

soma = num1 + num2
divi = num1 / num2
mult = num1 * num2
sub  = num1 - num2 

print("Resultado da soma", num1, "+", num2,"é:", soma)
print("Resultado da divisao", num1, "/", num2,"é:", divi)
print("Resultado da subtraçao", num1, "-", num2,"é:", sub)
print("Resultado da multiplicaçao", num1, "X", num2,"é:", mult)

# convertendo tipos de dados 
print()
print(30*"-", "Convertendo tipos de dados", 30*"-")

ano_nascimento = input("Digite seu ano de nascimento:")
print(type(ano_nascimento))
#convertendo para inteiro 
ano_nascimento = int(ano_nascimento)
print(type(ano_nascimento))

n1 = 10
n2 = 20 

print("A soma é:", n1+n2, type(n1), float(n2))
'''
saudacao = input("Digite seu nome: ")
cpf = input("DSigite seu CPF: ")
telefone = input("Digitre seu número de telefone")

print (20*"-", "Dados pessoais", 20*"-")
print(" Nome:", saudacao)
print("CPF:", cpf, "|telefone:", telefone)
print(60*"-")













