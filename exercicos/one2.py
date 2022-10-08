#conceitos de dicionário em python
                    # append(...[:]) não funciona para copiar um dicionário então para exercer essa função basta usar um método interno que é  .copy()
                    # Como não é possivel usar o enumerete no dicionário terá que usar o .items() para exercer essa função
                    # Para usar o print formatado é preciso colocar aspas duplas ex: print(f'O { dadoS["nome"] tem {dadoS["idade"]} anos.}')
                    # .items() > junta o keys e values em um só ex: ['nome':'Scarlxrd']['idade':18]['Sexo':'M']
                    # .keys() > retonar os id's cadastrado ex: nome,idade,sexo... 
                    # .values() > retorna os elementos que foram add ex: o nome da pessoa que foi digitados   
                    # Para remover um elemento de um dicionário basta colocar del o nome do dicionário e o id que será retirado ex: deldadoS=['idade']
                    # O .append não funciona no dicionário basta criar um id novo com o novo atributo exemplo: dadoS['sexo']='M' 
dados=dict()        #Dois jeitos de declarar um dicionário  
dadoS={'nome':'Scarlxrd','idade':18} #No dicionário no lugar de colocar o índici 0 ou 1 basta chamar pelo id já declarado no exem do lado        
filme={'titulo':'Jujutsu 0','Ano':'2022','Diretor':'Sunghoo Park'}
for k,v in filme.items():
    print(f'O {k} é {v}')
locadora=[{'Titulo':'Jujutsu 0','Ano':'2022','Diretor':'Sunghoo Park'},{'Titulo':'Matrix','Ano':'1999','Diretor':'Wachowski'},{'Titulo':'Vingadores Ultimato','Ano':'2019','Diretores':'Anthony Russo e Joe Russo'}]
print(locadora[2])

pessoa={'nome':'Scarlxrd','idade':18, 'sexo':'M'}
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos.')
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
del pessoa['sexo']
pessoa['nome']='Paulo'
pessoa['peso']=75.5
pessoa['sexo']='M'
for keys,valor in pessoa.items():
    print(f'{keys} = {valor}')

BraSil=[]
estado1={'uf':'Rio de Janeiro','sigla':'RJ'}
estado2={'Uf':'São Paulo','sigla':'SP'}
BraSil.append(estado1)
BraSil.append(estado2)
print(BraSil[1]['sigla'])

EsTADO={}
BRASiL=[]
for c in range(0,3):
    EsTADO['Uf']=str(input('Unidade Federativa: '))
    EsTADO['Sigla']=str(input('Sigla do estado: '))
    BraSil.append(EsTADO.copy())
for e in BRASiL:
    print(e)


