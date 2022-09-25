num=int(input('Digite um número [999 para parar] : '))
contador=0
soma=0
while num!=999:
    contador+=1
    soma+=num 
    num=int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(contador,soma))

