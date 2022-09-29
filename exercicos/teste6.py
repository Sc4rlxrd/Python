from time import sleep
num=[]
maior=0
menor=0
while True:
    for c in range (0,6):
        num.append(int(input(f'Digite um valor na posição {c}: ')))
        if c==0:
            maior=menor=num[c]
        else:
            if num[c]>maior:
                maior=num[c] 
            if num[c]<menor:
                menor=num[c]   
    print(f'Os valores digitados foram {num}')
    print(f'O maior número digitado foi {maior}')
    print(f'O menor número digitado foi {menor}')
    opcao=int(input('''Deseja continuar?
    [1] Sim
    [2] Não
    R: '''))
    if opcao==1:
        num.clear()
        while True:
            for c in range (0,6):
                num.append(int(input(f'Digite um valor na posição {c}:')))
                if c==0:
                    maior=menor=num[c]
                else:
                    if num[c]>maior:
                        maior=num[c] 
                    if num[c]<menor:
                        menor=num[c]   
            print(f'Os valores digitados foram {num}')
            print(f'O maior número digitado foi {maior}')
            print(f'O menor número digitado foi {menor}')
            
            break
            
    if opcao==2:
        print('OK...')
        print('Vamos encerrar o programa....')
        sleep(2.0)
        print('Volte sempre!!')
    break