
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
carros.append('Fusca') #add um novo valor
carros.pop() #remove o último valor
print(carros)
carros.append('Fusca')
carros.append('Monza')
carros.append('Marea')
carros.sort() #coloca em ordem 
carros.append('Fiesta')
print(f'Novos carros foram add {carros}')
carros.sort(reverse=True) #coloca em ordem revesa 
print(f'Em outra ordem {carros}')
carros.remove('Monza')
print(f' Monza foi removido da lista {carros}')
if 'Fusca' in carros: # se fusca estiver em carros remova ele
    carros.remove('Fusca')
print(f'Ficou assim agora {carros}')
carros.append('BMW Séries 3')
carros.append('BMW X')
carros.append('Land Rover Discpvery')
for c,objeto in enumerate(carros):
    print(f'Na posição {c} encontrei o  {objeto}!')
print('Cheguei ao final da lista...')
num=[]
for cont in range(0,5):
    num.append(int(input('Digite um valor:')))
for co,v in enumerate(num):
    print(f'Na posição {co} encontrei o valor {v}!')
print('Cheguei no final de outra lista...')    

A=[2,3,4,7]
B=A[:] # desse método eu copio a 1 lista na 2 como um backup da 1 lista 
B[2]=8
print(f'Lista A: {A}')
print(f'Lista B: {B}')

