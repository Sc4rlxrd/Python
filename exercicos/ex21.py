name = str(input('Digite o seu nome completo: ')).strip().upper()
print('Muito prazer em te conhecer!!')
n= name.split()
print('O seu primeiro nome é {}'.format(n[0]) )
print('O seu último nome é {}'. format( n [len(n)-1]  ))