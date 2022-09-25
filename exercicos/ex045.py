from random import randint
from time import sleep 
lista=('Pedra','Papel','Tesoura')
computador= randint(0,2) 

print('''Suas opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')

jogador=int(input('Qual é sua jogada?' ))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POOOO!!!!!')
sleep(1)
print('O computador jogou {}.'.format(lista[computador]))
print('Jogador jogou {}.'.format(lista[computador]))

if computador==0:  #computador jogou pedra

    if jogador ==0:
        print('EMPATE')

    elif jogador==1:
        print('JOGADOR VENCEU')

    elif jogador==2:
        print('COMPUTADOR VENCEU')

    else:
        print('JOGADA INVÁLIDA!')

elif computador==1:  #computador jogou papel

    if jogador ==0:
        print('COMPUTADOR VENCEU')

    elif jogador==1:
        print('EMPATE')

    elif jogador ==2:
        print('JOGADOR VENCEU')

    else:
        print('JOGADA INVÁLIDA!')    

elif computador==2:   #computador jogou tesoura

    if jogador == 0:
        print('JOGADOR VENCEU')

    elif jogador ==1:
        print('COMPUTADOR VENCEU')

    elif jogador == 2:
        print('EMPATE')

    else: 
        print('JOGADA INVÁLIDA!')   


