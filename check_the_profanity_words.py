import urllib.request

def read_the_file():

    file = 'words' # Pegando o arquivo a ser lido!

    texto = open(file) # Abrindo o arquivo e armazenando em uma variavel 'words'

    arquivo = texto.read()  # Lendo o arquivo

    texto.close() # Fechando o arquivo após lido!

    check_the_word(arquivo)

def check_the_word(arquivo):

    real = arquivo.replace(' ','%20')

    request = 'http://www.purgomalum.com/service/json?text='
    url = request + real

    request = urllib.request.urlopen(url)

    print (request.read())

read_the_file()