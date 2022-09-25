primeirotermo=int(input('Primeiro termo: '))
Razão=int(input('Razão: '))
decimo=primeirotermo + (10-1) * Razão
for x in range(primeirotermo,decimo+Razão,Razão):
    print(x)
print('Acabou!!')