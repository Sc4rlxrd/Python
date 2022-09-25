from datetime import date
 
atual= date.today().year
nascimento=int(input('Ano de nascimento:'))
idade=atual- nascimento
print('''Qual seu gênero: 
    [1] MASCULINO
    [2] FEMININO''')
opção=int(input('Qual opção: '))
if opção==2:
    print('Você não é obrigada a servir')
    print('Ainda dejesa servir?')
    print('''[1]SIM   [2]NÃO''')
    desejar=int(input('Qual sua opção: '))
    if  idade ==18:
     
     print('Você vai se alistar esse ano, FAÇA SUA INSCRIÇÃO IMEDIATAMENTE! ')
    elif idade < 18:
        tempo= 18 - idade
        print('Você não vai se alistar esse ano falta(m) {} ano(s)'.format(tempo))
        ano= atual - tempo
        print('Seu alistamento será em {}'.format(ano)) 

print('HELLO WORD!!')
        


