#dicionario

usuario = {
    'nome' : 'Pedro',
    'Idade' : 16
}
print(usuario)
print(type(usuario))

print(f'Nome: {usuario['nome']}')
print(f'idade: {usuario['Idade']}')
#print(f'Nome: {usuario['nome']}')
#print(f'idade: {usuario['Idade']}')

usuarios= ['pedro', 'gomes', 'cris','samu']
print(usuario)
print(f'Nome:{usuarios[-2]}')

print(f'Nome: {usuario.get('nome')}')