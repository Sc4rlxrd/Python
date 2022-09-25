
alfa=('A','B','C','E','D','G','F')
lanche=('Hambúrguer','Pizza','Suco','Pudim','Misto quente')

#tuplas são imutaveis 
for comida in lanche:
    print(f'Vou comer {comida}') #mostra comida na ordem até o indice final
print('Comi pra caramba!!!')

for contador in range(0,len(lanche)): #mostra a ordem dos alimentos sem aparecer o nome 
    print(lanche[contador])
print('Comi pra caramba!!!')

for posição,comida in enumerate(lanche): #o mais completo ele junta os dois de cima 
    print(f'Eu vou comer {comida} na posição:  {posição}')

print(sorted(alfa)) #em ordem alfabética 
print(alfa)

pessoa=('Scarlxrd','idade=17','Sexo:M')
print(pessoa)
#obs: del(ALGUMA VARIAVEL) com esse comando ele apaga a variavel escolhida

# Listas
carros=['Ferrari','Ferrari Monza','Mercedes-AMG Project One','Aston Martin Valkyrie','Bugatti Chiron Pur Sport','Lamborghini Veneno','Bugatti Centodieci']
print(f'Os carros que poucos tem na garragem: {carros}')
carros.append('Fusca')
carros.pop()
print(carros)
carros.append('Fusca')
carros.append('Monza')
carros.append('Marea')



