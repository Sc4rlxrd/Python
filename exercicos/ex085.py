num=[[],[]]
valor=0
for c in range(1,8):
    valor=int(input(f'Digite o {c}º um valor:'))
    if valor %2==0:
        num[0].append(valor)
    else:
        if valor %2==1:
            num[1].append(valor)
print('-='*30)      
num[0].sort()
num[1].sort()      
#print(f'Todos os valores: {num}')
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpars digitados foram: {num[1]}')

        

