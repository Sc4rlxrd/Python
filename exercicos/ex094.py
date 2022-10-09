tropa=list()
pessoa=dict()
soma=média=0
while True:
    pessoa.clear()
    pessoa['nome']=str(input('Nome: '))
    while True:
        pessoa['sexo']=str(input('Sexo:  [M/F]  ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade']=int(input('Idade: '))
    soma+=pessoa['idade']
    tropa.append(pessoa.copy())
    while True:
        resposta=str(input('Quer continuar [S/N]')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta=='N':
            break
print('=='*30)
print(f'A) Ao todo temos {len(tropa)} pessoas cadastradas.')
média=soma/len(tropa)
print(f'B) A média de idade é de {média:5.1f} anos.')
print('C) As mulheres cadastradas foram ', end=' ')
for p in tropa:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}, ', end=' ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in tropa:
    if p['idade']>=média:
        print('     ',end='')
        for k,v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<< ENCERRADO  >>')