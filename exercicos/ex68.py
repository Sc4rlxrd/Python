from random import randint
vitoria=0
derrota=0
while True:
    jogador=int(input('Digite um valor'))
    computador=randint(0,10)
    total=jogador+computador
    tipo= str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    if tipo=='P':
    
        if total%2==0:
            print('Você venceu')
            vitoria+=1
        else:
            print('Você perdeu')
            derrota+=1
            break
    elif tipo=='I':
        if total%2==1:
            print('Você venceu')
            vitoria+=1
        else:
            print('Você perdeu')
            derrota+=1
            break
    print('Vamos jogar novamente....')
print(f'Você jogou {jogador} e o computador {computador} e o total foi {total}')    
print(f'GAMER OVER!!! Você teve {vitoria} vitoriras e teve {derrota} derrotas')


