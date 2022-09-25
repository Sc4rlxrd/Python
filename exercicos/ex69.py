tot18=0
totH=0
totMenos20=0
while True:
    idade=int(input('Digite a idade:'))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('Digite o sexo: [M/F]')).upper().strip()
        if idade>=18:
            tot18+=1
        if  sexo=='M':
            totH+=1
        elif sexo=='F'and idade<=20:
            totMenos20+=1
    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('Deseja continuar? [S/N]')).upper().strip()
    if resposta=='N':
            break
print(f'O total de pessoa com {tot18} mais de 18 anos. ')
print(f'O total de homens cadastrado foi {totH}')
print(f'O total de mulheres cadastrada com menos com 20 foi {totMenos20}')  