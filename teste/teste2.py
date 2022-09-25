
from datetime import date 
atual=date.today().year 
quantdade=int(input('Quantos carros vão ser analizados?:  '))
totalmaior=0
totalmenor=0


for x in range(1,quantdade+1):
    carro=int(input('Qual o ano do {}º carro:'.format(x)))
    velho=30+carro
    if velho >= atual:
        totalmaior+=1
    else:
        totalmenor+=1
print('Carro a quantidade de carro velho {}'.format(totalmaior))
print('A quantidade de carro novo é {}'.format(totalmenor))