aluno={'nome':'','média':''}
aluno['nome']=str(input('Nome: '))
aluno['média']=float(input(f'Média de {aluno["nome"]}: '))
print('-='*30)
if aluno['média']>=7:
    aluno['situação']='Aprovado'

if 5<= aluno['média']<7:
    aluno['situação']='Recuperação'

if aluno['média']<5:
    aluno['situação']='Reprovado'  

for k,v in aluno.items():
    print(f'{k} é igual a {v}')


    
