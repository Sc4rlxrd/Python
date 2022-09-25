velo=float(input('QUAL A SUA VELOCIDADE ATUAL DO CARRO?'))
multa= (velo - 80 )*7
if velo>80:
    print('MULTADO!! Você exerceu o limite que é de 80km/h. Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança')