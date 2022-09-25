tupla=('Lapís',1.75,'Borracha' ,2.00,'Caderno' ,15.90,'Estojo',25.00,'Transfirador',4.20,'Compasso',9.99,'Mochila',120.00,'Canetas',22.30,'Livros',34.90 )
print('===='*10)
print('LISTAGEM DE COMPRAS')
print('===='*10)
for pos in range (0, len(tupla)):
    if pos %2==0:
        print(f'{tupla[pos]:.<30}', end='')
    else:
        print(f'{tupla[pos]:>7.2f}')
print('===='*10)
