palavras=('aprender','programar','linguagem','python','curso','grátis','estudar','praticar','trabalhar','mercado','programador','futuro')
for x in palavras:
    print(f'\n Na palavra {x.upper()} temos ', end='')
    for letra in x:
        if letra.lower() in 'aáeiou':
            print(letra,end=' ')