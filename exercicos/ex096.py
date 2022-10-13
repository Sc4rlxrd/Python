def personalizado(msg):
  print('='*25)
  print(msg)
  print('='*25)

def terreno(largura,comprimento):
  print(f'O terreno de {largura} de largura e {comprimento} de comprimento da o resultado {largura*comprimento}m² ')
personalizado('Controle de terrenos')
largura=float(input('Digite o valor da largura do terreno (m) : '))
comprimento=float(input('Digite o valor do comprimento do terreno (m): '))
terreno(largura,comprimento)