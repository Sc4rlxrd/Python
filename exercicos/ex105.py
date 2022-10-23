

def notas(*n,sit=False):
    """
        -> Função para analisar a situação de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indica se deve ou não adicionar a situação
        :return: dicionário com várias informações da turma
    """
    r=dict()
    r['total']=len(n)
    r['maior']=max(n)
    r['menor']=min(n)
    r['média']= sum(n)/len(n)
    if sit:
        if r['média']>=7:
            r['situação'] = 'Boa'
        elif r['média']>=5:
            r['situação']= 'Razoável'
        else:
            r['situação']= 'Ruim'
    return r

resp=notas(9.4,6,7.5,4.9, sit=True)
print(resp)
documents=int(input('''Deseja ver as docsstrings?
[1] SIM
[2] NÃO
R: '''))
if documents ==1:
    help(notas)
if documents ==2:
    print('Ok, Volte sempre')
    
