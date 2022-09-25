larg=float(input('Largura da parede:'))
Alt=float(input('Altura da parede:'))
área= larg*Alt
tinta=área/2
print('A dimensão de sua parede é {} x {}. A área e de {}m²'.format(larg,Alt, área))
print('Para pintar essa parede, você precisará de {} L de tinta'.format(tinta))