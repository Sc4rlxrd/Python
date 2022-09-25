peso=float(input('Digite seu peso? (Kg)     '))
altura=float(input('Digite sua altura?  (m)   '))
imc= peso/(altura**2)
print('O IMC dessa pessoa {:.1f}'.format(imc))
if imc <18.5:
    print(' Você está abaixo do PESO NORMAL')
elif imc >= 18.5 and imc <25:
    print('Você está no Peso ideal, PARABÉNS!')
elif imc >=25 and imc <30:
    print('Você está em Sobrepeso, cuidado!')
elif imc>=30 and imc<40:
    print('Você está com Obesidade, cuidado!')
elif imc >=40:
    print(' Você está com Obesidade mórbia, VÁ AO MÉDICO IMEDIATAMENTE!')

