def contador(i, f, p):
    """
        -> Faz uma contagem e mostra na tela.
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passos da contagem
        :return: sem retorno
    """ #Docsstrings
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM!')
help(contador) #Interactive help

def somar(a=0,b=0,c=0): # Parâmetros opcionais
    """
            -> Faz uma soma de três valores e mostra na tela.
            :param a: o primeiro valor
            :param b: o segundo valor
            :param c: o terceiro valor
    """ #Docsstrings
    s=a+b+c
    print(f'A somar vale {s}')

somar(3,2,5)
somar(8,4)
somar()
help(somar)#Interactive help

def teste(b):
    global a
    a=8
    b+=4
    c=2
    print(f'A dentro vale {a}') # a(local)
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
a=5
teste(a)
print(f'A fora vale {a}') # a(global)

def adição(a=0,b=0,c=0):
    s=a+b+c
    return s
r1=adição(3,2,5)
r2=adição(2,2,2)
r3=adição(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')


def fatorial(num=1):
    f=1
    for c in range(num,0,-1):
        f*=c
    return f
f1=fatorial(5)
f2=fatorial(4)
f3=fatorial()
print(f'Os resultados são  {f1}, {f2} e {f3}')
n=int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)} ')

def par(n=0):
    if n%2==0:
        return True
    else:
        return False

num=int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')


#Interactive help: função interna  ele mostra um manual de alguma função ou módulo 'help(alguma função ou módulo)'.
#Docsstrings: Vocẽ cria logo abaixo da def para poder consultar o "manual" mais completo sobre a def que você criou. Ex aspas duplas 3 vezes.
#Parâmetros opcionais: parâmetro opcinal seria uma segunda atribuição para a programa não quebrar ex: def somar(a,b,c=0) se não digitar o 3 valor a def ainda vai funcionar sem mostrar erro.
#Escopo de variáveis: variável criada fora da def ela tem o escopo global (pode se chamada em qualquer lugar) já variável criada dentro a def tem o escopo local (só funciona dentro da def aonde foi criada)
#^^^  cont...de cima Tem como usar o escopo global dentro da def basta usar a palavra reservada "global" ex: global a
#Return: retonar informações/ valores já definido por você antes.

