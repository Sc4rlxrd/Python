#UPDATE DO EXERCÍCIOS 95 EM PYTHON 
def linha():
  print('--==--'*15)

def título(txt):
  linha()
  print(txt)
  linha()

def dados():
  time=list()
  jogador=dict()
  partidas=list()
  while True:
      jogador.clear()
      jogador['nome']=str(input('Nome: '))
      tot=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
      partidas.clear()
      for c in range(0,tot):
          partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
      jogador['gols']=partidas[:]
      jogador['total']=sum(partidas)
      time.append(jogador.copy())
      while True:
          resposta=str(input('Quer continuar? [S/N]')).upper()[0]
          if resposta in 'SN':
              break
          print('ERRO! Responda apenas com S ou N')
      if resposta =='N':
              break
  linha()
  print('cod', end='')
  for i in jogador.keys():
      print(f'{i:<15}', end='')
  print()
 
  for k,v in enumerate(time):
      print(f'{k:>3} ', end='')
      for d in v.values():
          print(f'{str(d):<15}',end='')
      print()
  linha()
  while True:
      busca=int(input('Mostra dados de qual jogador? (999 para PARAR) '))
      if busca == 999:
          break
      if busca>= len(time):
          print(f'ERRO! Não existe jogador com código {busca}!')
      else:
          print(f'    -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
          for i,g in enumerate(time[busca]['gols']):
              print(f'    No jogo {i+1} fez {g} gols.')
      linha()
  print('<<   VOLTE SEMPRE    >>')
    
     
print(dados())
título('Scarlxrd')
título('UPDATE DO EXERCÍCIOS 95 EM PYTHON ')




