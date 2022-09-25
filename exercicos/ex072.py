
from time import sleep


cont=(' zero','um',' dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num=int(input('Digite um número entre 0 e 20: '))
    if 0<=num<=20:
        break
print(f'O número que você digitou: {cont[num]}')

resp=int(input('''Você deseja continuar?
[1] Sim
[2] Não
R: '''))
if resp==1:
    while True:
        num=int(input('Digite um número entre 0 e 20: '))
        if 0<=num<=20:
            break
    print(f'O número que você digitou: {cont[num]}')
else:
    print('Encerrando......')
    sleep(2)
    print('Pronto!! Volte sempre!!! ')