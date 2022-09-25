from random import randint
from time import sleep
num=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'Os valores sorteados foram: ')
for x in num:
    print(f'{x}')

print(f'O maior número sorteado foi {max(num)}')
print(f'O menor número sorteado foi {min(num)}')

resp=int(input('''Deseja continuar?
[1] SIM
[2] NÃO
R:'''))
if resp==1:
    while True:
        num=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
        print(f'Os valores sorteados foram:', end='')
        for x in num:
            print(f'{x}')
        print(f'O maior o número sorteado foi {max(num)}')
        print(f'O menor número sorteado foi {min(num)}')
        break
elif resp==2:
    print('Tudo bem. Vamos encerrar o programa.....')
    sleep(1.5)
    print('VOLTE SEMPRE!!!') 
