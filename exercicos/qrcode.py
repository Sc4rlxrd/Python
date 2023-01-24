import qrcode 
imagem=qrcode.make('https://mangalivre.net/')
imagem.save("meuqrcode.jpg")

# Antes de executar o código 
# faça isso: pip install pyshorteners