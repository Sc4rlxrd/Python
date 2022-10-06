expressão=str(input('Digite uma expressão: '))
pilha=[]
for símb in expressão:
    if símb == '(':
        pilha.append('(')
    elif símb==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão não está valida!')