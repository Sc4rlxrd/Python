import moeda

p=float(input('Digite um valor: R$'))
print(f'A metade de {moeda.moeda(p)} é R${moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é R${moeda.dobro(p)}')
print(f'Aumento de 10%: R${moeda.moeda(moeda.aumentando(p,10))}')
print(f'Diminuindo em 10%: R${moeda.moeda(moeda.diminuir(p,10))}')
print('BANCO SCARLXRD')