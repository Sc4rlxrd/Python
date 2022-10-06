lista=[]
par=[]
impar=[]
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta=str(input('Quer continuar? [S/N]'))
    if resposta in 'Nn':
        break
for i,v in enumerate(lista):
    if v %2==0:
        par.append(v)
    elif v %2==1:
        impar.append(v)
print('=-'*30)
print(f'A lista competa é {lista}')
print(f'Lista de pares é {par}')
print(f'Lista de ímpares é {impar}')