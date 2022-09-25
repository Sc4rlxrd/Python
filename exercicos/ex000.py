import random
n1=str(input('Digite um produto que devo comprar:'))
n2=str(input('DIgite outro produto que devo comprar:'))
n3=str(input('Digite outro produto que devo comprar:'))
n4=str(input('Digite outro produto que devo comprar:'))
compras=[n1,n2,n3,n4]
escolhido=random.choice(compras)
print('Vou comprar {}'.format(escolhido))