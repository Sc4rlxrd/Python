from operator import itemgetter
from random import randint
from time import sleep
jogo={'Jogador1': randint(1,6),
      'Jogador2': randint(1,6),
      'Jogador3': randint(1,6),
      'Jogador4': randint(1,6)}
ranking=dict()
print('Valores sorteados')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1.5)
ranking=sorted(jogo.items(),key=itemgetter(1),reverse=True)
print('-=-'*25)
print('  == RANKING DOS JOGADORES ==  ')
for i,v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1.5)
