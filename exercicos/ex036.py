casa=float(input('Qual vai ser o valor da casa?R$'))
salário=float(input('Qual é seu salário? R$'))
ano=float(input('Quantos anos de financiamento?'))
prestação= casa/(ano*12)
minimo=salário*30/100
print('Para pagar um casa de R${:.2f} em {} anos'.format(casa,ano))
print('A prestação será de R${:.2f}'.format(prestação))
if prestação<= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')


