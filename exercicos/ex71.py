print('=='*30)
print('             BANCO SCARLXRD.IO                  ')
print('=='*30)
print()
num=float(input('Digite o valor do saque?'))
total=num
céd=200
totalcéd=0
while True:
    
    if total>=céd:
        total-=céd
        totalcéd+=1
    else:
        if totalcéd>0:
            print(f'Total de {totalcéd} cédulas de R${céd}')
        if céd==200:
            céd=100
        elif céd==100:
            céd=50
        elif céd==50:
            céd=20
        elif céd==20:
            céd=10
        elif céd==10:
            céd=5
        elif céd==5:
            céd=1
        elif céd==1:
         céd=0
        totalcéd=0
        if total==0:
            break 

