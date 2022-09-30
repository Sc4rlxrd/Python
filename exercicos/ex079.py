valores=[]
while True:
    num=int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar... ')
    resposta=str(input('Quer continuar? [S/N]'))
    if resposta in 'Nn':

        break
valores.sort()
print('=-'*30)
print(f'Você digitou os valores {valores}')
