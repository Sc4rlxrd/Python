from datetime import date
atual=date.today().year
nascimento=int(input('Ano de nascimento: ')) 
idade= atual-nascimento
print('''Qual é o seu sexo:
[1] MASCULINO
[2] FEMININO''')
sexo=int(input('Qual é sua opção:'))
print('Quem nasceu em {} tem {} em {}'.format(nascimento,idade,atual))
if sexo == 2:
    print('Você não precisa se alistar!')
elif  idade == 18:
    print('Você vai se alistar esse ano, FAÇA SUA INSCRIÇÃO IMEDIATAMENTE!')
elif idade < 18:   
    tempo= 18 - idade
    print('Você não vai se alistar esse ano falta(m) {} ano(s)'.format(tempo))
    ano= atual + tempo
    print('Seu alistamento será em {}'.format(ano))
    
elif idade > 18:
    tempo= idade-18
    ano= atual-tempo
    print('Você já passou do tempo de alistar há {} ano(s)'.format(tempo))
    print('Seu alistamento foi no ano {}'.format(ano))
    
