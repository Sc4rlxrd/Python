total=0
totalmil=0
barato=''
menorpreço=0
cont=0
while True:
    produto=str(input('Nome do produto:'))
    preço=float(input('Preço: R$'))
    cont+=1
    total+=preço
    if preço>=1000:
        totalmil+=1
    if cont==1:
        menorpreço=preço
        barato=produto
    else:
        if preço<menorpreço:
            menorpreço=preço
            barato=produto
    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resposta=='N':
            break
print('Acabou!!!')
print(f'total da compras foi R${total}')
print(f'Temos {totalmil} produtos com mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R$:{menorpreço}')
