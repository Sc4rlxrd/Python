
print('>'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('>'*30)
n=int(input('Quantos termos você quer mostrar? '))
t1=0 # Primeiro termo 
t2=1 # Segundo termo
print('{} > {}  '.format(t1,t2),end='')
contador=3 # Terceiro termo 
while contador<=n:
    t3=t1+t2
    print(' > {}'.format(t3),end='')
    t1=t2
    t2=t3 
    contador+=1

print(' > FIM!')
