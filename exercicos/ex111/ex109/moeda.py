def aumentando(preço=0, taxa=0,formato=False):
    res=preço+(preço*taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preço=0, taxa=0,formato=False):
    res=preço-(preço*taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço=0,formato=False):
    res=preço *2
    return res if formato is False else moeda(res)

def metade(preço=0,formato=False):
    res= preço /2
    return res if formato is False else moeda(res)

def moeda( preço=0 ,moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')

def resumo( preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço,True)}')
    print(f'{taxaa}% de aumento: \t{aumentando(preço,taxaa,True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço,taxar,True)}')
    print('-'*30)

def LeiaDinheiro(msg):
    valido=False
    while not valido:
        entrada=str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro:\"{entrada}\" é um preço inválido!\033[m')
        else:
            valido=True
            return float(entrada)

def LeiaInt(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor