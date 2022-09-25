from math import comb
n=int(input('Digite o valor de N: '))
k=int(input('Digite o valor de K: '))
while n<0:
    n=int(input('Digite o valor de N: '))
while k<0:
    k=int(input('Digite o valor de K:'))
conta=comb(n,k)
print(f'A combinação com os números {n} e {k} dão o resultado {conta}')