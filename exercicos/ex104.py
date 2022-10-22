def leiaInt(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('\033[0;31m ERRO! Digite um número válido. \033[m')
        if ok:
            break
    return valor    #colocar cor no terminal basta usar o código (\033[0;cod da corm] e no final \033[m) obs: tudo isso dentro das aspas

n=leiaInt('Digite um número:  ')
print(f'\033[0;36m Você acabou de digitar o número {n} \033[m')

