from pytube import YouTube, Playlist

# OBs: ANTES DE TUDO USAR O ( pip install pytube ) DEPOIS SO EXECTUTAR O CÓDIGO.

# Digite o link do vídeo e o local que deseja salvar o video #

link = input("Digite o link do vídeo que deseja baixar:  ")
path = input("Digite o diretório que deseja salvar o vídeo:  ")
yt = YouTube(link)

# Mostra os detalhes do video #
print("Título: ", yt.title)
print("Número de views: ", yt.views)
print("Tamanho do vídeo: ", yt.length, "segundos")
print("Avaliação do vídeo: ", yt.rating)

# Usa a maior resolução #
ys = yt.streams.get_highest_resolution()

# Começa o Download do vídeo #
print("Baixando...")
ys.download(path)
print("Download completo!")

# Opção de fazer o download de uma playlist  #

resposta=int(input('''Você desejar fazer download de uma playlist?
[1] SIM
[2] Não
R:'''))

if resposta ==1:
    
        playlist = Playlist(input('Digite o link da playlist que deseja baixar: '))
        path = input('Destino do download: ')
        print(f'Iniciando o download dos vídeos da playlist: {playlist.title}\n')

        for indice, video in enumerate(playlist.videos):
            
            print(f'Baixando vídeo {indice + 1}/{len(playlist)}')
            
            video.streams.get_highest_resolution().download(path)
        
        print('Todos os vídeos foram baixados!')
    

if resposta ==2:
    
        print('OK....')
        print('VOLTE SEMPRE...')


    
  