from random import randint
from time import sleep
lista=[]
jogos=[]
print('='*30)
print('         JOGA NA MEGA SENA         ')
print('='*30)
quant=int(input('Quantos jogos você quer que eu sorteia pra ti? '))
total=1
while total<=quant:
    cont=0
    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total+=1
print('-='*3, f'SORTEANDO {quant} JOGOS', '-='*3)
for índice,l in enumerate(jogos):
    print(f'Jogo {índice+1}: {l}')
    sleep(1.5)
print('-='*5, '<  BOA SORTE!!  >','-='*5 )

