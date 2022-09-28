
n=0
s=0
while True:
    n=int(input('Digite um número: '))
    if n==999:
        break
    s+=n
print('A soma vale {} '.format(s))


############################################ Teste 2:

n1=0
so_ma=0
contador=0
while True:
    n1=int(input('Digite um número: '))
    if n1==999:
        break
    so_ma+=n1
    contador+=1
print(f'A soma vele {so_ma}')
print('você mostrou {} números'.format(contador))

############################################## Teste 3:

nome=''
idade=0
endereço=''
while idade<18:
    idade=int(input('Digite a idade do responsável...'))
nome=str(input('Informe o nome completo: ')).strip().upper()
endereço=str(input('Informe seu endereço: ')).strip().upper()
print(f'O {nome} tem {idade}  anos e mora no endereço {endereço} ')

from time import sleep 
print('Olá')
sleep(1.5)
print('Tchau!!')