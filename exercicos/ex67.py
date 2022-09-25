while True:
    num=int(input('Quer ver a tabuada de qual valor: '))
    if num<0:
        break
    for c in range(1,11):
        print(f'{num} X {c}= {num*c}')

print('Programa de Tabuada encerrado. Volte sempre!')