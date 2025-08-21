import os

while True:
    try:
        #usuario informa o nome do arquivo
        arquivo= input('Digite o nome do arquivo (sem extensão): ').lower().strip()

        #abre arquivo
        with open(f'{arquivo}.txt', 'r', encoding= 'utf-8') as f:
            arquivo_aberto= f.read()

        os.system('cls' if os.name == 'nt' else 'clear')

        #mostra os dados do arquivo
        print(arquivo_aberto)
        while True:
            prosseguir  = input('Deseja abriri outro arquivo?(s/n)').strip().lower()
            if prosseguir == 's' or prosseguir == "n":
                break
            else:
                print('Opção inválida')
                continue
        match prosseguir:
            case 's':
                continue
            case 'n' :
                break

    except Exception as e :
        print(f'Não foi possível ler o arquivo. {e}')
        continue