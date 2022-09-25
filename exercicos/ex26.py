distencia= float(input('Qual é a distância da sua viagem?'))
print('----'*30) # deixar mais bonito no console
print('Você está prestes a começar uma viagem de km {}'.format(distencia))
print('----'*30) # deixar mais bonito no console
if distencia <=200:
    preço=distencia*0.50
else:
    preço=distencia*0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
