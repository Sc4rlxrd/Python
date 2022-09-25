
totaldemulher20=0
maioridadehomem=0
nomevelho=''
somadasidades=0
mediaidade=0
for x in range(1,5):
    print('{}ª Pessoa'.format(x))
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input(' Sexo [M/F]: ')).upper().strip()
    somadasidades+=idade
    if x==1 and sexo=='M':
        maioridadehomem=idade
        nomevelho=nome 
    elif sexo=='M' and idade>maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    elif sexo=='F' and idade<20:
        totaldemulher20+=1
mediaidade=somadasidades/4
print('A média de idade do grupo é de {:.2f} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totaldemulher20))