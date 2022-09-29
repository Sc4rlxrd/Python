valores=[]
maior=0
menor=0
for c in range (0,5):
    valores.append(int(input(f'Digite um valor na posição {c}:')))
    if c==0:
        maior=menor=valores[c]
    else:
        if valores[c]>maior:
            maior=valores[c]
        elif valores[c]<menor:
            menor=valores[c]
print('=-'*30)
print(f'Você digitou os valores {valores}')
print(f'O maior número digitado foi {maior} nas posições ', end='')
for i,v in enumerate(valores):
    if v==maior:
        print(f'{i}...', end='') # (i)= indice
print() 
print(f'O menor número digitado foi {menor} nas posoções ', end='')
for i,v in enumerate(valores):
    if v==menor:
        print(f'{i}...', end='') 
print()