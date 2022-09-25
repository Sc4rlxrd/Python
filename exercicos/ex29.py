salário=float(input('Qual é o valor do funcionário? R$'))
if salário <=1250:
    novo=salário+(salário*15/100)#calculando o salário com 15% de aumento
else:
    novo=salário+(salário*10/100)#calculando o salário com 10% de aumento
print('Quem ganhava r${:.2f} passa a ganhar r${:.2f} agora'.format(salário,novo))