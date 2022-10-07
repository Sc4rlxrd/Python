matrix = [[0,0,0],[0,0,0],[0,0,0]]
for largura in range(0,3):
    for coluna in range(0,3):
        matrix[largura][coluna] = int(input(f'Digite um valor para {largura},{coluna}: '))
print('=-'*30)
for largura in range(0,3):
    for coluna in range (0,3):
        print(f'[{matrix [largura][coluna]:^5}]', end='')
    print()