from random import randint
from time import sleep

def sorteia(lista):
    print('SORTEANDO 5 VALORES DA LISTA ')
    for c in range(0,5):
        n=randint(0,10)
        lista.append(n)
        print(f'{n}  ', end='', flush=True)
        sleep(0.3)
    print('PRONTO')
def somarPar(lista):
    soma=0
    for valor in lista:
        if valor%2==0:
            soma+=valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

números=list()
sorteia(números)
somarPar(números) 