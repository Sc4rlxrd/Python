soma=0
contador=0
for x in range(1,501,2):
    if x %3==0:
        contador=contador+1
        soma=soma+x 
print('A soma de todos os {} valores solicitados é {} '.format(contador,soma))
