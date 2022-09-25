frase=str(input('Digite uma frase: ')).strip().upper()
conjunto=frase.split()
junto=''.join(conjunto)
inverso=''
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
if inverso==junto:
    print('Temos um POLÍNDROMO!')
else:
    print('A frase acima NÃO forma um POLÍNDROMO!')

