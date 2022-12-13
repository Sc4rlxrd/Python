import math

def fatorial(num):
    c=num #contador 
    f=1 #fatorial
    print('Calculando {}! = '.format(num), end='')

    while c>0:
        print('{}'.format(c),end='')
        print(' X ' if c >1 else ' = ', end='') 
        f*=c
        c-=1
    print('{}'.format(f))

def dobro(num):
    return num*2

def triplo(num):
    return num*3

def adição(num,num2):
    return num+num2

def menos(num,num2):
    return num-num2

def multiplicação(num,num2):
    return num*num2

def divisão(num,num2):
    return num/num2

def raiz(num):
    raiz = math.sqrt(num)
    return raiz

def potenciação(num,num3):
    poten=num**num3
    return poten

def coseno(num):
    return math.cos(num)

def seno(num):
    return math.sin(num)

def tangente(num):
    return math.tan(num)


def logbase(num):
    return math.log10(num)
