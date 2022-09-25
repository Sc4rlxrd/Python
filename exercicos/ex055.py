maior=0
menor=0
for x in range(1,6):
    peso=float(input('Peso da {}ª pessoa.'.format(x)))
    if x==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        elif peso<menor:
            menor=peso
print('O maior peso lido foi de {}Kg.'.format(maior))
print('O menor peso lido foi {}Kg.'.format(menor))
