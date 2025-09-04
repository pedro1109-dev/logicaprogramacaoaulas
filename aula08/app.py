import random
import string
import json
def gerar_senha(comprimento=12,incluir_maiusculo=True, incluir_minusculo=True,
               incluir_numeros=True, incluir_caracter= True):
    
    caracteres = ''
    if incluir_maiusculo:
        caracteres += string.ascii_uppercase

    if incluir_minusculo:
        caracteres += string.ascii_lowercase

    if incluir_numeros:
        caracteres += string.digits

    if incluir_caracter:
        caracteres += string.punctuation

    if not caracteres:
        return ValueError('Deve ter pelo menos um tipo de carcater') 
    
    senha = ''.join(random.choice(caracteres)for _ in range(comprimento))
    print(f'Senha: {senha}')
    return senha

def main():
    print('Gerador de senhas fortes ')
    comprimento = int(input('Digite o comprimento da senha(padrão é 12): ')or 12)
    incluir_maiusculo = input('Incluir maiúsculo (s/n, padrão = sim): ').lower() != 'n'
    incluir_minuscula = input('Inclir minúsculo (s/n, padrão = sim): ').lower() != 'n'
    incluir_numeros = input('Inclir números (s/n, padrão = sim): ').lower() != 'n'
    incluir_caracter_esp = input('Inclir carcater especial (s/n, padrão = sim): ').lower() != 'n'

    senha = gerar_senha(comprimento, incluir_maiusculo, incluir_minuscula,
                        incluir_numeros, incluir_caracter_esp)
    
    print(f'A senha foi gerada: {senha}')

    with open('senhas.txt', 'a' ) as s:
        s.write(f'\n{senha}')


if __name__=='__main__':
    main()