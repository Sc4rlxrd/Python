n=str(input('VAMOS COMEÇAR A CONTAGEM REGRESSIVA: '))
for  contagem in range (10,0,-1):
    print(contagem)

######
x=int(input('Digite um número: '))
for teste2  in range (0,x+1):
    print(teste2)
print('fim')
########
inicio=int(input('Inicio: '))
fim=int(input('Fim: '))
pular=int(input('Pular: '))
for teste3 in range (inicio, fim+1, pular):
    print(teste3)
print('FIM!!!')
#####
s=0
for teste4 in range(0,3):
    c=int(input('Digite um valor: '))
    s +=  c
print('A soma entre os valores digitados são: {}'.format(s))    