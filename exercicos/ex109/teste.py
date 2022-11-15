import moeda

p=float(input('Digite um valor: R$'))
print(f'A metade de {moeda.moeda(p)} é R${moeda.metade(p,True)}') #TRUE PARA FORMATAR A MOEDA EM PT-BR  E FALSE RETURN EM MODELO EUA 
print(f'O dobro de {moeda.moeda(p)} é R${moeda.dobro(p,True)}')
print(f'Aumento de 10%: R${moeda.aumentando(p,10,True)}')
print(f'Diminuindo em 10%: R${moeda.diminuir(p,10,True)}')
print('~'*30)
print('     BANCO MOEDA SCARLXRD       ')
print('~'*30)