
from time import sleep
########################################################################################### INFORMAR O SEXO DO USUÁRIO

sexo=str(input('Informe seu sexo:  [M/F] ')).strip().upper()
while sexo not in 'MmFf':
    sexo=str(input('Informação incorreta. Informe o sexo corretamente: ')).upper()
print('Sexo {} Registrado com sucesso.'.format(sexo))
########################################################################################### PEDINDO A IDADE DA PESSOA 
idade=int(input('Informe sua idade: '))
while idade <18:
     idade=int(input('Informe a idade do responsavel: '))
print('Idade {} Resgidtrdo com sucesso.'.format(idade))
######################################################################################### PEDINDO  O NOME DO USUÁRIO
nome=str(input('Informe o nome do usuário: ')).upper().strip()
###############  CONFERINDO DADOS
if nome == nome:
    confimardados=str(input('''Dados estão corretos? 
    Sexo: {}
    Nome: {}
    Idade: {}'''.format(sexo,nome,idade))) 
    opção=int(input('''
    [1] SIM
    [2] NÃO
    R:'''))
    if opção==1:
        print('Ok, Vamos prosseguir: ')
        endereço=str(input('Informe o endereço:')).strip().upper()
        pai=str(input('Informe nome do Pai completo: [Se não tiver deixe em branco]: ')).strip().upper()
        mae=str(input('Informe o nome da Mãe completo: ')).strip().upper()         
        confimando2=str(input('''Dados estão corretos?
        Sexo: {}
        Nome: {}
        Idade: {}
        Nome do Pai: {}
        Nome da Mãe: {}
        Endereço: {} '''.format(sexo,nome,idade,pai,mae,endereço)))
        enviar=int(input('''Deseja enviar o formulário?
        [1] SIM
        [2] Não
        R:'''))
        if enviar ==1:
            print('Ok, Vamos enviar.....')
            sleep(1)
            print('Enviado com sucesso.')
            sleep(2.0)
            print('=='*30)
            print('PROGRAMA FINALIZADO.')
            print('VOLTE SEMPRE!!!')
            print('=='*30)
        elif enviar==2:
            motivo=int(input('''Qual motivo?
            [1] Dados errados
            [2] Não quero mais enviar o formulário
            [3] Outro
            R: '''))
            if motivo==1:
                sexo=str(input('Informe o sexo: ')).strip().upper()[0]
                nome=str(input('Informe o nome de usuário: ')).strip().upper()
                idade=int(input('Informe a idade: '))
                while idade<18:
                    idade=int(input('Informe a idade do responsável: '))
                pai=str(input('Informe o nome do Pai completo:  [Se não tiver pai deixe em branco]  ')).strip().upper()
                mae=str(input('Informe o nome da Mãe completo: ')).strip().upper()
                endereço=str(input('Informe o endereço: ')).strip().upper()
                correto=str(input(f'''Estão corretos os dados?
                Sexo:{sexo}
                Nome:{nome}
                Idade:{idade}
                Nome do Pai:{pai}
                Nome da Mãe:{mae}
                Endereço:{endereço}'''))
                deseja=int(input('''Deseja enviar o formulário? 
                    [1] SIM
                    [2] NÃO
                    R: '''))
                if deseja=='1':
                    print('Ok. Iremos enviar o formulário...')
                    sleep(1.5)
                    print('Formulário enviado com sucesso...')
                    sleep(2.0)
                    print('=='*30)
                    print('PROGRAMA FINALIZADO.')
                    print('VOLTE SEMPRE!!!')
                    print('=='*30)
                    
                elif deseja=='2':
                    print('Ok. Iremos cancelar o envio do formulário...')
                    sleep(1.8)
                    print('Envio cancelado...')
                    sleep(2.0)
                    print('=='*30)
                    print('PROGRAMA FINALIZADO.')
                    print('VOLTE SEMPRE!!!')
                    print('=='*30)
            elif motivo==2:
                pergunta=int(input('''Qual motivo?
                [1] Não gostou do site
                [2] Perdeu o interesse
                R: '''))
                if pergunta==1:
                    print('É uma pena, Espero que volte... ')
                    print('Vamos cancelar o envio...')
                    sleep(1.5)
                    print('Cancelado....')
                    sleep(2.0)
                    print('=='*30)
                    print('PROGRAMA FINALIZADO.')
                    print('VOLTE SEMPRE!!!')
                    print('=='*30)
                if pergunta==2:
                    print('É uma pena, Espero que volte...')
                    print('Vamos cancelar o envio...')
                    sleep(1.5)
                    print('Cancelado...')
                    sleep(2.0)
                    print('=='*30)
                    print('PROGRAMA FINALIZADO.')
                    print('VOLTE SEMPRE!!!')
                    print('=='*30)
            elif motivo==3:
                print('Vamos cancelar...')
                sleep(1.5)
                print('Cancelado....')
                sleep(2.0)
                print('=='*30)
                print('PROGRAMA FINALIZADO.')
                print('VOLTE SEMPRE!!!')
                print('=='*30)
            elif motivo==3:
                print('Ok. Iremos cancelar o envio do formulário.....')
                sleep(1.5)
                print('Cancelado....')
                sleep(2.0)
                print('=='*30)
                print('PROGRAMA FINALIZADO.')
                print('VOLTE SEMPRE!!!')
                print('=='*30)
    elif opção==2:
        sexo=' '
        while sexo not in 'MF':
            sexo=str(input('Informe o sexo: [M/F] ')).strip().upper()[0]
        nome=str(input('Informe o nome do usuário: ')).strip().upper()
        idade=int(input('Informe a idade: '))
        while idade<18:
            idade=int(input('Informe a idade do responsável: '))
        correto=str(input(f'''Os dados estão corretos?
        Sexo:{sexo}
        Nome:{nome}
        Idade:{idade}'''))
        proseguir=' '
        while proseguir not in 'SN':
             proseguir=str(input('Deseja prosseguir? [S/N]')).upper().strip()[0]
             if proseguir=='S':
                print('OK...Espere um momento')
                sleep(1.9)
                print('Esta tudo pronto...')
                endereço=str(input('Informe o seu endereço: ')).upper().strip()
                pai=str(input('Informe o nome do seu Pai completo: [Se não tiver pai deixe em branco]')).strip().upper()
                mae=str(input('Informe o nome da sua Mãe completo: ')).upper().strip()
                coreto=str(input(f'''Dados estão certos?
                Sexo: {sexo}
                Nome: {nome}
                Idade: {idade}
                Nome do Pai: {pai}
                Nome da Mãe: {mae}
                Endereço: {endereço}'''))
                certo=' '
                while certo not in 'SN':
                    certo=str(input('Deseja continuar? [S/N]')).upper().strip()[0]
                if certo=='S':
                    print('Vamos enviar')
                    print('Espere um momento...')
                    sleep(2.0)
                    print('Enviado com sucesso...')
                    sleep(2.0)
                    print('=='*30)
                    print('PROGRAMA FINALIZADO.')
                    print('VOLTE SEMPRE!!!')
                    print('=='*30)

                if certo=='N':
                    print('Ok. Vamos cancelar o envio...')
                    sleep(2.0)
                    print('Cancelado com sucesso...')
                    sleep(2.0)
                    print('=='*30)
                    print('PROGRAMA FINALIZADO.')
                    print('VOLTE SEMPRE!!!')
                    print('=='*30)
                    break
             if proseguir=='N':
                print('Vamos cancelar o envio...')
                print('Espere um momento...')
                sleep(2.0)
                print('Cancelado com sucesso...')
                print('Vamos voltar ao início.')
                break
        sleep(2.0)
        print('=='*30)
        print('PROGRAMA FINALIZADO.')
        print('VOLTE SEMPRE!!!')
        print('=='*30)

