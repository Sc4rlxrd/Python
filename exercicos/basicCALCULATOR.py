from time import sleep

def adicao(num1=0,num2=0):
   
    return num1+ num2

def menos(num1=0,num2=0):
    
    return num1-num2 

def multiplicação(num1=0,num2=0):
    
    return num1*num2

def divisão(num1=0,num2=0):
   
    return  num1/num2

def linha():
    print('~'*50)

num1=float(input('Digite o 1º número: '))
num2=float(input('Digite o 2º número: '))
resp=int(input('''Qual operação você deseja escolher? 
[1] ADIÇÃO
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO
R: '''))
if resp ==1:
    linha()
    print(f' O resultado da adição de {num1} e {num2} deu o resultado: {adicao(num1,num2)}')
    
elif resp == 2:
    linha()
    print(f'O resultado dos valores {num1} e {num2} deu o resultado: {menos(num1,num2)} ')

elif resp ==3:
    linha()
    print(f'O resultado dos valores {num1} e {num2} deu o resultado: {multiplicação(num1,num2)}')

elif resp ==4:
    linha()
    print(f'O resultado dos valores {num1} e {num2} deu o resultado: {divisão(num1,num2)} ')
    
linha()
sleep(1.5)
print('Volte Sempre!!!')