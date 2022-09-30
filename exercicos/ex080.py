lista=[]

for c in range(0,5):
    num=int(input('Digite um valor:'))
    if c==0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista... ')
    else:
        posição=0
        while posição<len(lista):
            if num<=lista[posição]:
                lista.insert(posição,num)
                print(f'Adicionado na posição {posição} da lista')
                break
            posição+=1

print('-='*30)
print(f'Os valores digitados foram {lista}')