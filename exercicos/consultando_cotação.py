"""
CONSUMINDO API PÚBLICA PARA ACESSAR COTAÇÃO DE ALGUMAS MOEDAS. 

"""
import requests
import json

cotação= requests.get(' https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotação=cotação.json()
while True:
    opção=int(input('''Qual moeda deseja consultar? 
                    [1] Dólar (USD)
                    [2] Euro (EUR) 
                    [3] Bitcoin (BTC)
                    R: '''))
    if opção == 1:
        cotação_dólar=cotação['USDBRL']['bid']
        print(f'R$:{cotação_dólar}')
    if opção == 2:
        cotação_euro=cotação['EURBRL']['bid']
        print(f'R$:{cotação_euro}')
    if opção == 3:
        cotação_bitcoin=cotação['BTCBRL']['bid']
        print(f'R$:{cotação_bitcoin}')
        
    print('-'*25)
    parar=int(input('''Deseja Parar?
    [1] Sim
    [2] Não
    R: '''))
    if parar == 1:
        print('-'*25)
        print('VOLTE SEMPRE!!'.center(25))
       
        print('-'*25)
        break
    print('-'*25)

