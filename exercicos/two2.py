from time import sleep

def dados(nome, idade, sexo, endereço,mãe):
    print(f'''Os dados estão corretos?
Nome: {nome}
Idade: {idade}
Sexo: {sexo}
Endereço: {endereço}
Nome da Mãe: {mãe}''')
nome=str(input('Digite o seu nome: ')).upper()
idade=int(input('Digite sua idade: '))
sexo=str(input('Informe o seu sexo: [M/F]')).upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('ERRO!.Informe o seu sexo: [M/F]')).upper()[0]
endereço = str(input('Informe o seu endereço: ')).upper()
mãe=str(input('Digite o nome de sua Mãe: ')).upper()


resposta = str(input('Quer continuar? [S/N]')).upper()[0]
while resposta not in 'SsnN':
    resposta = str(input('Informação incorreta. Informe somente S ou N ')).upper()[0]
    if resposta in 'Ss':
        print('Ok, Vamos continuar em breve.')
    if resposta in 'Nn':
        print('Ok vamos continuar em breve.')
        break


def formulário():
    enviar=int(input('''Deseja enviar o formulário?
             [1] Sim
             [2] Não
             R: '''))
    if enviar ==1:
                 print('Ok, iremos enviar agora mesmo  espera um momento.')
                 sleep(1.0)
                 print('Enviado com sucesso...')
                 print('VOLTE SEMPRE!')
    if enviar ==2:
                print('Ok, vamos cancelar o envio, espera um momento ')
                sleep(1.5)
                print('Cancelado com sucesso...')
                motivo=int(input('''Qual motivo? 
                 [1] DADOS ERRADOS.
                 [2] NÃO QUERO MAIS ENVIAR O FORMULÁRIO.
                 [3] OUTRO
                 R: '''))
                if motivo==1:
                    nome = str(input('Digite o seu nome: ')).upper()
                    idade = int(input('Digite sua idade: '))
                    sexo = str(input('Informe o seu sexo: [M/F]')).upper()[0]
                    while sexo not in 'MmFf':
                        sexo = str(input('ERRO!.Informe o seu sexo: [M/F]')).upper()[0]
                    endereço = str(input('Informe o seu endereço: ')).upper()
                    mãe = str(input('Digite o nome de sua Mãe: ')).upper()
                    enviar1 = int(input('''Deseja enviar o formulário?
                                 [1] Sim
                                 [2] Não
                                 R: '''))
                    if enviar1 == 1:
                        print('Ok, iremos enviar agora mesmo  espera um momento.')
                        sleep(1.0)
                        print('Enviado com sucesso...')
                        print('VOLTE SEMPRE!')
                    if enviar1 == 2:
                        print('Ok, vamos cancelar o envio, espera um momento ')
                        sleep(1.5)
                        print('Cancelado com sucesso...')
                if motivo==2:
                    print('Ok, VOLTE SEMPRE!!')
                    sleep(0.9)
                    print('PROGRAMA FINALIZADO...')
                    sleep(1.0)
                    print('VOLTE SEMPRE!!')
                if motivo==3:
                    print('Ok, QUALQUER DÚVIDA ACESSAR O SITE: GITHUB.COM/Sc4rlxrd')
                    sleep(0.9)
                    print(('PROGRAMA FINALIZANDO...'))
                    sleep(1.0)
                    print('VOLTE SEMPRE!!')






dados(nome, idade, sexo, endereço,mãe)
formulário()
sleep(0.5)
print('UPDATE DO ARQUIVO CHAMADO two.py')
