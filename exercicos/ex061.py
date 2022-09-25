print('GERADOR DE PA')
print('=='*10)
one_termo=int(input('Primeiro termo: '))
razão=int(input('Razão da PA: '))
termo=one_termo
contador=1
while contador <=10:
    print('{} > '.format(termo), end='')
    termo+=razão
    contador+=1
print('FIM!')