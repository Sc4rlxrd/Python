def fatorial(n,show=False):
    """
        -> Calcula o fatorial de um número
        :param n:  o número a ser cálculado.
        :param show: (opcional) Mostrar ou não a conta.
        :return: o valor do fatorial de um número.
    """
    f=1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c >1:
                print(' x ', end='')
            else:
                print(' = ' , end='')
        f*=c
    return f

def linha():
    print('~'*30)

fat=int(input('Digite um número para saber o fatorial: '))
resposta=int(input('''Deseja ver o cálculo?
[1] SIM
[2] NÃO
R: '''))
if resposta == 1:
    print(fatorial(fat,True))
if resposta ==2:
    print(fatorial(fat,False))

linha()

documents=int(input('''Deseja ver as docsstrings?
[1] SIM
[2] NÃO
R: '''))
if documents ==1:
    help(fatorial)
if documents ==2:
    print('OK,Volte Sempre')
