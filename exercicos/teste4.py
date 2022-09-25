for x in range (1,10):
    print(x)
print('FIM!!')

######
x1=0
while x1<10:
    print(x1)  
    x1=x1+1
print('FIM!!!2')
########
n=1
soma=0
while n!=0:
    n=int(input('Digite um valor: '))
    soma+=1
print('FIm')
print('A soma entre os número digitados são {}'.format(soma))
#####

r='S'
while r=='S':
    n=int(input('Digite um valor: '))
    r=str(input('Deseja continuar? [S/N]')).upper()
print('FIm')
########
n=1
par=0
ímpar=0
while n!=0:
    n=int(input('Digite um valor: '))
    if n!=0:
        if n%2==0:
         par+=1
        else:
            ímpar+=1
print('Você digitou tantos pares {} e tantos ímpares {}'.format(par,ímpar))