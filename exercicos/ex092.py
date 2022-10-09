from datetime import datetime
dados=dict()
dados['nome']=str(input('Nome:'))
nasc=int(input('Ano de nascimento:'))
dados['idade']= datetime.now().year - nasc
dados['ctps']=int(input('Carteira de Trabalho (0 não tem): '))
dados['sexo']=str(input('Sexo: [M/F]'))

if dados['ctps']!=0:
    dados['contratação']=int(input('Ano de Contratação: '))
    dados['salário']=float(input('Salário: R$'))
    if dados['sexo'] in 'Mm':
        dados['aposentadoria']= dados['idade']+((dados['contratação'] +35)- datetime.now().year)
    if dados['sexo'] in 'Ff':
        dados['aposentadoria']= dados['idade'] + ((dados['contratação']+30)-datetime.now().year)
print('='*30)
for k,v in dados.items():
    print(f' {k} tem o valor {v}')
