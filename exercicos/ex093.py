
jogo=dict()
partidas=[]
jogo['nome']=str(input('Nome do jogador: '))
tot=int(input(f'Quantas partidas {jogo["nome"]} jogou? '))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogo['gols']=partidas[:]
jogo['total']= sum(partidas)
print('=-'*30)
print(jogo)
print('=-'*30)
for k,v in jogo.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {jogo["nome"]} jogou {len(jogo["gols"])} partidas')
for i, v in enumerate(jogo['gols']):
    print(f'     => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogo["total"]} de gols')
