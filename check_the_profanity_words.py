import urllib.request

def read_the_file():

    escolha = input("Qual arquivo deseja verificar? \n --> ")
    arquivo = open(escolha)
    contents = arquivo.read()
    arquivo.close()
    check_the_word(contents)

def check_the_word(arquivo):

    arquivo_tratado_sem_espaco = arquivo.replace(' ','%20')
    arquivo_tratado_sem_quebra_linha = arquivo_tratado_sem_espaco.replace('\n', '%20')

    request = 'http://www.purgomalum.com/service/json?text='
    url = request + arquivo_tratado_sem_quebra_linha

    request = urllib.request.urlopen(url)

    print (request.read())

read_the_file()