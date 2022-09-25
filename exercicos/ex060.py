n=int(input('Digite o número que para calcular seu  fatorial:  '))
c=n #contador 
f=1 #fatorial
print('Calculando {}! = '.format(n), end='')

while c>0:
    print('{}'.format(c),end='')
    print(' X ' if c >1 else ' = ', end='') 
    f*=c
    c-=1
print('{}'.format(f))