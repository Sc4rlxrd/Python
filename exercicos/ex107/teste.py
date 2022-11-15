import moeda

p=float(input('Digite um valor: R$'))
print(f'A metade de {p} é R${moeda.metade(p)}')
print(f'O dobro de {p} é R${moeda.dobro(p)}')
print(f'Aumento de 10%: R${moeda.aumentando(p,10)}')
print(f'Diminuindo em 10%: R${moeda.diminuir(p,10)}')
