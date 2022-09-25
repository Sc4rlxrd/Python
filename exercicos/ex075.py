from itertools import count


núm=(int(input('Digite um número: ')),int(input('Digite outro número: ')),int(input('Digite mais um número: ')),int(input('Digite o último número: ')))
print(f'Você digitou esses números {núm}')
print(f'O número 9 apareceu {núm.count(9)}ª vezes')
if 3 in núm:
    print(f'O número 3 apareceu na posição {núm.index(3)+1}')
else:
    print('O número 3 não foi digitado....')
print(f'Os valores pares digitados foram: ', end=' ')
for x in núm:
    if x %2==0:
        print(x, end=' ')

