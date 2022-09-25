primeiro=int(input('Digite o valor de casos favoráveis: '))
segundo=int(input('Digite o valor de casos possívieis: '))
conta=primeiro/segundo
cem=100
porcentagem=primeiro*cem
porcentage_m=porcentagem/segundo
print(f'A probabilidade dos números {primeiro} e {segundo} e a resposta é {conta}')
print(f'A porcentegem dos valores acima é {porcentage_m:.1f}% ')