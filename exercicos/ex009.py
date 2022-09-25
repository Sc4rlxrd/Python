dias=int(input('Quantos dias alugados?'))
km=float(input('Quantos Km rodados?'))
pago=(dias*60)+(km*0.15)
print('O valor ser pago é de R${:.2f}'.format(pago))