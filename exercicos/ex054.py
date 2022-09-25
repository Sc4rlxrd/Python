from datetime import date 
atual=date.today().year
totalmaior=0
totalmenor=0
for x in range (1,8):
    nascimento=int(input('Em que ano a {}ª pessoa nasceu?'.format(x)))
    idade=atual-nascimento
    if idade>=21:
        totalmaior+=1
    else:
        totalmenor+=1
print('Tivemos {} maiores de idade.'.format(totalmaior))
print('Tivemos {} menores de idade'.format(totalmenor))
   
