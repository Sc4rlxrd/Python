preço=float(input('Preços das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('''
[1] à vista dinheiro/cheque    
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''') 
opcão=int(input('Qual é a opção?'))
if opcão==1:
    desconto= preço - (preço*10/100)
    print('De R${:.2f} você ira pagar {:.2f} houve um desconto de 10%'.format(preço,desconto))
elif opcão ==2:
    desconto=preço-(preço*5/100)
    print('De {:.2f} R$ você ira pagar {:.2f} houve um desconto de 5% '.format(preço,desconto))
elif opcão==3:
    x=preço/2
    print('Sua compra será parcelada em 2x você ira pagar R${:.2f}  SEM JUROS'.format(x))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,preço))
elif opcão==4:
    total=preço+(preço*20/100)
    totaldeparcelas=int(input('Quantas parcelas?'))
    parcela=total/totaldeparcelas
    print('Sua compra será parcelada em {:.2f}x de R${:.2f}  COM JUROS'.format(totaldeparcelas,parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço,total))
else:
    print('ERRO 404:FIle not found. SAI CALOTEIRO KKKKKKKKKKKKKKKKKKKKKK')
