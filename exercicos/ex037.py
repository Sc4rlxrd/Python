inteiro=int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimanl''')
opção=int(input('Sua opção:'))
if opção==1:
    print('{} convertido em Binário é igual a {}'.format(inteiro,bin(inteiro)[2:]))

elif opção==2:
    print('{} convertido em octal é igual a {}'.format(inteiro,oct(inteiro)[2:]))

elif opção==3:
    print('{} convertido em hexadecimal é igual a {}'.format(inteiro,hex(inteiro)[2:]))
else:
    print('Opção não encontrado. tente novamente.')    