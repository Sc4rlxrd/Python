from random import randint
computador = randint(1,6) # Faz o computador sortear  um número entre (0 á 5)
print('-==-'*20)
print('Vou pensar em número entre 1 e 6. Tente advinhar....')
print('-==-'*20)
jogador= int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar o número
if jogador==computador:
    print('PARABÉNS! Você conseguir me  vencer!')
else:
    print('GANHEI! eu pensei no número {} e não no {} '.format(computador,jogador))
