nota1 = float(input(('Digite a primeira nota:')))
nota2 = float (input( ('Digite a segunda nota:')))
nota3 = float (input(('Digite a terceira nota:')))
nota4 = float (input('Digite a quarta nota:'))
média = (nota1+nota2+nota3+nota4)/2
print('A sua média foi {:.1f}'.format(média))
if média >=6.0:
    print('Sua média foi boa! PARABÉNS!!!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')


