soma=0
contador=0
for x in range(1,7):
    num=int(input('Digite o {}° valor: '.format(x)))
    if num %2==0:
     soma= soma+num 
     contador= contador+1
print('Você informou {} números Pares e a soma foi {}'.format(contador,soma ))    