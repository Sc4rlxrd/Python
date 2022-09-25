
num=int(input('Digite um valor: '))
totaldedivisival=0
for x in range(1,num+1):
    
    if num %x==0:
        print('\033[33m')
        totaldedivisival=totaldedivisival+1
    else:
        print('\033[31m')
    print('{}'.format(x))
print('\n\033[m O número {} foi divisível {} vezes'.format(num,totaldedivisival))
if totaldedivisival==2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')