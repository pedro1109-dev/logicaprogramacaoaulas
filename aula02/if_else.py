#FIXME - concatenação com +
'''
nome = "Pedro"
idade = 17
altura = 1.75
#saida de dados 
print ("Meu nome é:" + nome +", tenho" + str(idade)+"anos de idade")

#FIXME -concatenação com ,
print("Ola, meu nome é, ", nome, ",tenho", idade, "anos de idade")

#FIXME - concatenação com format
print("Ola, meu nome é,{}, tenho {} anos de idade".format(nome , idade))

#FIXME - concatenação com f-string
print(f"Ola, meu nome é {nome} e tenho {idade}  anos de idade")


# eliminando quebra de linha 
print(" O sabio sabia ", end="")
print("que o sabiá sabia assobiar.")


valor = 1.23456789
# exibindo o vaor com duas casas depois da virgula 
print(f"{valor:.2f}")
print(30*'=')
peso = input('Digite seu peso: ').replace(',','.')
peso = float(peso)
print(f'{peso:.2f}'.replace('.',','))

 #tipos de variaveis 
 #Atividade 1 de sala
nome = "pedro"
idade = 16
ano_de_nasc = 2008
altura = 1.75
ativo = True

print("Meu nome é:", nome ,type(nome))
print("tenho:", idade , "de anos" ,type(idade))
print("tenho:", altura , "de altura" ,type(altura))
print("nasci em:", ano_de_nasc ,type(ano_de_nasc))
print("Meu tipo de variavel é :", ativo ,type(ativo))



# O uso do if else
#Estrutura de decsão
nome = input('Digite seu nome:')
idade = int(input('Digite a sua idade:'))

print("Antes do if")
if idade >= 18:
    print(f'{nome} é maior de idade.')
else:
    print(f'{nome} é menor de idade')

print(40*"-", "BOLETIM ESCOLAR", 40*"-") # .upper - caixa alta; lower - caixa baixa
nome_aluno = input("Digite o nome do aluno aqui:").upper()
nota1 = float(input("Digite a sua primeira nota:"))
nota2 = float(input("Digite a sua segunda nota:"))
nota3 = float(input("Digite a sua terceira nota:"))
nota4 = float(input("Digite a sua quarta nota:"))

media = (nota1 + nota2 + nota3 + nota4)/4
# >= 7 : aprovado
# >= 5 : recuperação 
# reprovado 
if media >= 7:
   print(f'{nome_aluno}!!Aluno Aprovado')
   print(f'Nota1: {nota1} |Nota 2:{nota2}')
   print(f'Nota3: {nota3} |Nota 4:{nota4}')
   print(20*'-')
   print(f'Média: {media}')
elif media >= 5:
   print(f'{nome_aluno}!!Aluno de recuperação')
   print(f'Nota1: {nota1} |Nota 2:{nota2}')
   print(f'Nota3: {nota3} |Nota 4:{nota4}')
   print(20*'-')
   print(f'Média: {media}')
else:
   print(f'{nome_aluno}!!Aluno Reprovado')
   print(f'Nota1: {nota1} |Nota 2:{nota2}')
   print(f'Nota3: {nota3} |Nota 4:{nota4}')
   print(20*'-')
   print(f'Média: {media}')
   '''
   # Requisitos mínimos
nome = input('Digite seu nome nesse espaço:')
idade = int(input('Digite sua idade aqui:'))
altura = float(input('Digite sua altura:'))

   #Verificação
if idade >= 12 or altura >= 1.2 :
      print(f'A entrada de {nome} está autorizada.')
else: 
      print(f'A entrada de {nome} não está autorizada.')

# variaveis 
print(40*"-","Verificação", 40*"-")
nome = input("Digite seu nome :")
idade = int(input("Digite sua idade:"))

print(nome, "é maior de idade." if idade >= 18 else " é menor de idade.")




