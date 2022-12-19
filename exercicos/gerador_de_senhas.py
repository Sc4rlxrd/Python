def gerador_senhas():

    import random 
    carácters_list='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789#@$%&!'
    quantidade=input('Digite qual tamanho da senha: ')
    carácters=random.choices(carácters_list,k=int(quantidade))
    new_senha=''.join(carácters)
    print(new_senha)
   
    guarda_senhas={new_senha}
    print(guarda_senhas)
    
gerador_senhas()