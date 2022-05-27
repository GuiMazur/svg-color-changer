import glob
import os
import codecs
import sys
import shutil

color = input('Insira o código Hex da cor nova(com #) / : ')
colorname = input('Insira o nome da sua cor: ')

try: #Muda o diretório para a pasta do main.py
    os.chdir(sys.argv[0].rsplit('\\', 1)[0])
except:
    pass
try:
    os.chdir(sys.argv[0].rsplit('/', 1)[0])
except:
    pass

try: #Cria a pasta 'assets-cor'
    os.mkdir('assets-{}'.format(colorname))
except:
    shutil.rmtree('assets-{}'.format(colorname))
    os.mkdir('assets-{}'.format(colorname))

for file in glob.glob('./assets/*.svg'): #Pega os nomes dos arquivos em um for
    with codecs.open(file, encoding='utf-8', errors='ignore') as f: #Abre o arquivo
        oldfile = f.read() #Transforma o arquivo em String             
    oldcolor = oldfile.split('stroke="')[1].split('"')[0]                   
    newfile = oldfile.replace(oldcolor, color) #Troca a cor antiga pela nova
    name = file.split("\\")[1].split(".")[0] #Pega o nome do arquivo (sem o diretório e sem o '.svg')
    with open('./assets-{}/{}.svg'.format(colorname, name), 'w') as n: #Salva a String como arquivo
        n.write(newfile)
    
