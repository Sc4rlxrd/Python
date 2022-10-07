temporário=[]
principal=[]
maior=menor=0
while True:
    temporário.append(str(input('Nome: ')))
    temporário.append(float(input('Peso: ')))
    if len(principal)==0:
        maior=menor=temporário[1]
    else:
        if temporário[1]>maior:
            maior=temporário[1]
        if temporário[1]<menor:
            menor=temporário[1]
    principal.append(temporário[:])
    temporário.clear()
    resposta=str(input('Quer continuar? [S/N]'))
    if resposta in 'Nn':
        break
print('=-='*30)
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end="")

for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end="")
print()

print(f'O menor peso foi de {menor}Kg. Peso de ',end='')
for p in principal:
    if p[1]==menor:
        print(f'[{p[0]}]',end='')
print()
