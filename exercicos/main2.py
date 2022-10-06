teste=list()
teste.append('Guilherme')
teste.append(18)
galera=list()
galera.append(teste[:])  #para criar uma copia da primeira lista precisa colocar o nome da lista que vai ser copiada e colocar colchetes e dois pontos EX: ....apend(teste[:])
teste[0]='Maria'
teste[1]=9
galera.append(teste[:])
print(f'{galera}')

########################################### Parte 2 

gAlera=[]
dados=[]
totalmaior=0
totalmenor=0
for c in range (0,3):
    dados.append(str(input('Nome:  ')))
    dados.append(int(input('Idade:  ')))
    gAlera.append(dados[:])
    dados.clear()
for p in gAlera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade. ')
        totalmaior+=1
    else:
        print(f'{p[0]} é menor de idade. ')
        totalmenor+=1
print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade> ')

############################################# Parte 3 

pessoal=[['Guilherme',18], ['Scarlxrd', 18], ['Peppa Pig',5],['George Pig',1.5]]
for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos de idade. ')

