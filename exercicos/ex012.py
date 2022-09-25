import math
num= float(input('Digite o ângulo que você deseja: '))
seno=math.sin(math.radians(num))
cosseno=math.cos(math.radians(num))
tan=math.tan(math.radians(num))
print('O ângulo de {} tem o seno {:.2f} '.format(num,seno))
print('O ângulo de {} tem o cosseno {:.2f}'.format(num,cosseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(num,tan))
