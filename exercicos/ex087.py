matrix=[[0,0,0],[0,0,0],[0,0,0]]
somar_par=maior=somar_coluna=0
for linha in range(0,3):
    for coluna in range(0,3):
        matrix[linha][coluna]=int(input(f'Digite um valor para {linha},{coluna}:'))
print('=-'*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matrix [linha][coluna]:^5}]', end="")
        if matrix [linha][coluna] %2==0:
            somar_par+=matrix[linha][coluna]
    print()
print('=-'*30)
print(f'A soma dos valores pares é {somar_par}')
for linha in range (0,3):
    somar_coluna+=matrix [linha][2]
print(f'a soma dos valores da 3 coluna é {somar_coluna}')
for c in range(0,3):
    if c ==0:
        maior=matrix[1][coluna]
    else:
        if matrix[1][coluna]> maior:
            maior=matrix[1][coluna]
print(f'O maior valor da 2 linha é {maior}')
