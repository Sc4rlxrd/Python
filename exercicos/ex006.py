produto=float(input('Qual é o preço do produto? R$'))
desconto= (produto*35/100)
print('O produto que custava {:.2f}, na promoção com desconto de 35% vai custar R${:.2f}'.format(produto,desconto))