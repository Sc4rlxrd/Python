nome = str(input('Digite seu nome: '))
if nome=='Guilherme':
    print('Que belo nome! {}'.format(nome))
elif nome=='Pedro' or nome=='Maria' or nome=='Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome=='Ana'or nome=='Claúdia'or nome=='Julia'or nome=='jessica':
    print('Belo nome feminino, {}'.format(nome))
else:
    print('Você tem um nome bem normal kkk')
print('Tenha um bom dia, {}!'.format(nome))