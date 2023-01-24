import pyshorteners

# URL original #
url = 'https://github.com/Sc4rlxrd/Python'

# Carrega lib #
s = pyshorteners.Shortener()

# Gera URL encurtada #
shortUrl = s.tinyurl.short(url)

# Mostra resultado #
print(f"URL Encurtada: {shortUrl}")



# Antes de executar o código 
# faça isso: pip install pyshorteners
