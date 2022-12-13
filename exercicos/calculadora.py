from UTEIS import numeros

print('~'*30)
print('CALCULADORA DO SCARLXRD')
print('~'*30)
while True:
    num = float(input(('Digite um valor: ')))
    num2 = float(input('Digite outro valor: '))
    resposta = int(input('''QUAL OPÇÃO ARITMÉTICA?
    [1] ADIÇÃO
    [2] SUBTRAÇÃO
    [3] MULTIPLICAÇÃO
    [4] DIVISÃO
    [5] RAIZ 
    [6] POTENCIAÇÃO
    [7] SENO
    [8] COSENO
    [9] TANGENTE
    [10] LOGARITMO
    [11] FATORIAL 
    R: '''))
    if resposta == 1:
        print(f'A soma entre {num} e {num2}  : {numeros.adição(num, num2)}')
    if resposta == 2:
        print(f'A subtração entre {num} e {num2} : {numeros.menos(num, num2)}')
    if resposta == 3:
        print(f'A multiplicação entre {num} e {num2} : {numeros.multiplicação(num, num2)}')
    if resposta == 4:
        print(f'A divisão entre {num} e {num2} : {numeros.divisão(num, num2)}')
    if resposta == 5:
        print(f'A raiz do {num} : {numeros.raiz(num)}')
    if resposta == 6:
        num3 = int(input('Digite o numero que sera elevado: '))
        print(f'A potenciação do {num} : {numeros.potenciação(num, num3):.1f}')
    if resposta == 7:
        print(f'O seno do {num} : {numeros.seno(num)}')
    if resposta == 8:
        print(f'O coseno do {num} : {numeros.coseno(num)}')
    if resposta == 9:
        print(f'A tangente do {num} : {numeros.tangente(num)}')
    if resposta == 10:
        print(f'O logaritmo  do {num} : {numeros.logbase(num)}')
    if resposta == 11:
        print(f'O fatorial do {num} : {numeros.fatorial(num)}')
    print('~'*30)
    para=str(input('Deseja parar?  [S/N]   ')).upper().strip()[0]
    while para not in 'SsNn':
        para = str(input('Deseja parar?  [S/N]   ')).upper().strip()[0]
    if para in 'S':
        break

print('Volte Sempre!')



#Modularização: SURGIU NO INÍCIO DA DÉCADA DE 60
#^FOCO: DIVIDIR UM PROGRAMA GRANDE
#^FOCO: AUMENTAR A LEGIBILIDADE
#BASTA CRIAR UM ARQUIVO .PY DENTRO DA MESMA PASTA E DEPOIS IMPORTA COM EXEMPLO ACIMA.

#VANTAGENS DA MODULARIZAÇÃO:
#1: ORGANIZAÇÃO DO CÓDIGO
#2: FACILIDADE NA MANUTENÇÃO
#3: OCULTAÇÃO DE CÓDIGO DETALHADO
#4: REUTILIZAÇÃO EM OUTROS PROJETOS


#PACOTES OU BIBLIOTECAS
#BASTA  CRIAS UMA PASTA PARA CADA MODULARIZAÇÃO OBS: PRECISAR TER UM ARQUIVO CHAMADO ( __init__.py )