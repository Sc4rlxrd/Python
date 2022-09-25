sexo=str(input('Informe seu sexo: [M/F] ')).strip().upper()
while sexo not in 'MmFf':
    sexo=str(input('Dados inválidos. Por favor verefique o sexo informado:')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))
    

'''sex='M','F'
for x in range (sex,5):
    nom=str(input('DIgite seu nome: '))
    sex=str(input('Digite seu sexo:  [M/F]')).upper()'''