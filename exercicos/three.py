from math import sqrt

print('Equação do 2º grau da forma: ax²+bx+c')
a=int(input('Digite o valor de A: '))
if a==0:
    print('Se A valer 0, não é equação do segundo grau. Tchau!!')
else:
    b=int(input('Digite o valor de B: '))
    c=int(input('Digite o valor de C:'))
    
    delta=b*b-(4*a*c)
    if delta<0:
        print('Delta menor que 0. Raízes imaginárias. Tchau!!')
    elif delta==0:
        raiz=-b/(2*a)
        print(f'Delta = 0, raiz = {raiz}')
    else:
        raiz1=(-b+ sqrt(delta)) / (2*a)
        raiz2=(-b- sqrt(delta)) / (2*a)
        print(f'Raízes: x1{raiz1} e x2{raiz2} ')
        print(f'Delta Δ{delta}')